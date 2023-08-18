import pygame

from other.unit_parameters import Colors


class Global:
    walls = set()
    enemies = set()
    bullets = set()
    bonuses = set()
    hero = None
    levelCreator = None
    menu = None
    keys = None
    backgroundColors = (Colors.SKY1, Colors.SKY2, Colors.SKY3, Colors.SKY4, Colors.SKY5,
                        Colors.SKY6, Colors.SKY7, Colors.SKY8, Colors.SKY9, Colors.SKY10)
    wallColors = (Colors.WALL1, Colors.WALL2, Colors.WALL3, Colors.WALL4, Colors.WALL5,
                  Colors.WALL6, Colors.WALL7, Colors.WALL8, Colors.WALL9, Colors.WALL10)

    SCREEN_SIZE = (1000, 1000)

    screen = pygame.display.set_mode(SCREEN_SIZE)

    FPS = 60
    g = 0.5
    worldSpeed = 1
    difficult = 1
    maxDifficult = 10
    gameOver = True
    pause = False

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
