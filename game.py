import random

import pygame as pg
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
BG_COLOUR = pg.Color(80, 60, 70)
PLAYER_COLOUR = pg.Color(90, 140, 190)
ENEMY_COLOUR = pg.Color(190, 90, 210)

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pg.Surface((75, 25))
        self.surf.fill(PLAYER_COLOUR)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pg.Surface((20, 10))
        self.surf.fill(ENEMY_COLOUR)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()

ADD_ENEMY = pg.USEREVENT + 1
pg.time.set_timer(ADD_ENEMY, 250)

player = Player()

enemies = pg.sprite.Group()
all_sprites = pg.sprite.Group()
all_sprites.add(player)

running = True

while running:
    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

        elif event.type == ADD_ENEMY:
            enemy = Enemy()
            enemies.add(enemy)
            all_sprites.add(enemy)

    pressed_keys = pg.key.get_pressed()

    player.update(pressed_keys)
    enemies.update()

    screen.fill(BG_COLOUR)

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Update the display
    pg.display.flip()
    clock.tick(60)

