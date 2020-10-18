import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

