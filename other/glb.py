import pygame


class Global:
    SCREEN_SIZE = (1000, 1000)
    walls = set()
    enemies = set()
    bullets = set()
    bonuses = set()
    hero = None
    screen = pygame.display.set_mode(SCREEN_SIZE)
    worldSpeed = 2
    g = 0.5
    keys = None
    difficult = 1
    maxDifficult = 10
    titles = None

    @staticmethod
    def screenWidth():
        return Global.SCREEN_SIZE[0]

    @staticmethod
    def screenHeight():
        return Global.SCREEN_SIZE[1]
