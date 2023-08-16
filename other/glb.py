import pygame


class Global:
    walls = set()
    enemies = set()
    bullets = set()
    bonuses = set()
    hero = None
    levelCreator = None
    menu = None
    keys = None

    SCREEN_SIZE = (1000, 1000)
    screen = pygame.display.set_mode(SCREEN_SIZE)

    FPS = 60
    g = 0.5
    worldSpeed = 1
    difficult = 1
    maxDifficult = 10
    gameOver = True

    @staticmethod
    def screenWidth():
        return Global.SCREEN_SIZE[0]

    @staticmethod
    def screenHeight():
        return Global.SCREEN_SIZE[1]

    @staticmethod
    def resetGame():
        Global.difficult = 1
        Global.gameOver = True
        Global.worldSpeed = 1

    @staticmethod
    def setsIsEmpty():
        return len(Global.walls) + len(Global.enemies) + len(Global.bullets) + len(Global.bonuses) == 0

