from pygame import Surface

from other.unit_parameters import Pair


class Global:
    def __init__(self):
        self.screen = None
        self.hero = None
        self.walls = None
        self.enemies = None

    def initGlobal(self, screen: Surface, hero, walls, enemies):
        self.screen = screen
        self.hero = hero
        self.walls = walls
        self.enemies = enemies
