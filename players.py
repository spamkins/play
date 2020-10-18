import random

import pygame as pg
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT
)

from config import App

SCREEN_WIDTH = App.config("SCREEN_WIDTH")
SCREEN_HEIGHT = App.config("SCREEN_HEIGHT")
PLAYER_COLOUR = App.config("PLAYER_COLOUR")
ENEMY_COLOUR = App.config("ENEMY_COLOUR")


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

