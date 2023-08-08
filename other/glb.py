import pygame


class Global:
    SCREEN_SIZE = (500, 500)
    walls = []
    enemies = []
    bullets = set()
    hero = None
    screen = pygame.display.set_mode(SCREEN_SIZE)
    worldSpeed = 0
    g = 0.5
