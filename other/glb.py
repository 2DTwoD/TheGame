import pygame


class Global:
    SCREEN_SIZE = (500, 500)
    walls = set()
    enemies = set()
    bullets = set()
    hero = None
    screen = pygame.display.set_mode(SCREEN_SIZE)
    worldSpeed = 2
    g = 0.5
    keys = None
