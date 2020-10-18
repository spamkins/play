import pygame as pg

class App:
    __conf = {
        "SCREEN_WIDTH": 800,
        "SCREEN_HEIGHT": 600,
        "BG_COLOUR": pg.Color(80, 60, 70),
        "PLAYER_COLOUR": pg.Color(90, 140, 190),
        "ENEMY_COLOUR": pg.Color(210, 90, 90)
    }
    __setters = []

    @staticmethod
    def config(name):
        return App.__conf.get(name)

    @staticmethod
    def set(name, value):
        if name in App.__setters:
            App.__conf[name] = value
        else:
            raise NameError("Name not accepted in set() method")

