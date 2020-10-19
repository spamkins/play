import random

import pygame as pg
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

from config import App
from players import Player, Enemy

SCREEN_WIDTH = App.config("SCREEN_WIDTH")
SCREEN_HEIGHT = App.config("SCREEN_HEIGHT")
BG_COLOUR = App.config("BG_COLOUR")

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

    if pg.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False

    # add a method here:
    
    # if(online) {
    #       updateNetwork() or updateServer() 
    
    # which just takes the position of your player, and any enemies, or any relevant state of the game.
    # - this would be cool because while it can just be empty for now, it could be extended to post the position of your
    # player onto someone else running instance, and then you could have a receive method, which will just render other players
    # on your existing game (and respond to their movements). While they can't interact at the moment, it would be cool and
    # I don't mind designing the networking and all that.
        
    # Update the display
    pg.display.flip()
    clock.tick(60)

