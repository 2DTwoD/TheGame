import codecs
import itertools

import pygame

from other.glb import Global
from other.unit_parameters import Colors


class Menu:
    def __init__(self):
        pygame.font.init()
        self.titleFont = pygame.font.SysFont('Times New Roman', 80)
        self.menuFont1 = pygame.font.SysFont('Times New Roman', 30)
        self.menuFont2 = pygame.font.SysFont('Times New Roman', 20)
        self.gameFont = pygame.font.SysFont('Times New Roman', 20, bold=True)
        self.color = Colors.WHITE
        self.scoreTable = {}

        self.newScore = False
        self.gamerName = 'Anonymous'
        self.inputRect = pygame.Rect(0, Global.screenHeight() / 2, 0, 40)

        self.blink = True
        self.blinkCount = 0

        try:
            file = codecs.open("scores.txt", "r")
            for line in file:
                name, score = line.split("@")
                score = int(score.removesuffix('\n'))
                self.scoreTable[name] = score
            file.close()
        except Exception as ex:
            print(ex)

    def inputTextHandler(self, event):
        if event.type == pygame.KEYDOWN:
            if Global.gameOver:
                if self.newScore:
                    if event.unicode == '@':
                        return
                    if event.key == pygame.K_BACKSPACE:
                        self.gamerName = self.gamerName[:-1]
                    elif event.key != pygame.K_RETURN:
                        if len(self.gamerName) < 30:
                            self.gamerName += event.unicode
                    if event.key == pygame.K_RETURN:
                        if self.gamerName.strip() == '':
                            self.gamerName = 'Anonymous'
                        if self.gamerName in self.scoreTable:
                            if Global.hero.score > self.scoreTable[self.gamerName]:
                                self.scoreTable[self.gamerName] = Global.hero.score
                        else:
                            self.scoreTable[self.gamerName] = Global.hero.score
                        self.scoreTable = dict(sorted(self.scoreTable.items(), key=lambda item: item[1], reverse=True))
                        self.scoreTable = dict(itertools.islice(self.scoreTable.items(), 10))
                        with open("scores.txt", "a") as file:
                            file.truncate(0)
                            for name, score in self.scoreTable.items():
                                file.write(f'{name}@{score}\n')
                        self.newScore = False
                else:
                    if event.key == pygame.K_RETURN and Global.setsIsEmpty():
                        Global.gameOver = False
                        Global.hero.reInit()
                        Global.levelCreator.reInit()
                        Global.pause = False
                        self.newScore = True
            else:
                if event.key == pygame.K_p:
                    Global.pause = not Global.pause

                if event.key == pygame.K_m:
                    self.newScore = False
                    Global.gameOver = True
                    Global.pause = not Global.pause

    @staticmethod
    def getSurfaceText(font, text, color, y, zeroX=False):
        surface = font.render(text, True, color)
        x = 0 if zeroX else Global.screenWidth() / 2 - surface.get_width() / 2
        Global.screen.blit(surface, (x, y))

    def getMenu(self):
        if self.blinkCount > 20:
            self.blinkCount = 0
            self.blink = not self.blink
        else:
            self.blinkCount += 1
        if Global.gameOver:
            if self.newScore:
                self.getSurfaceText(self.titleFont, f'TheGameOver', Colors.getRandom(),
                                    3 * Global.screenHeight() / 10)
                self.getSurfaceText(self.menuFont1, f'Your scores: {Global.hero.score}', Colors.BLUE,
                                    16 * Global.screenHeight() / 40)
                self.getSurfaceText(self.menuFont1, 'Enter your name:', self.color,
                                    18 * Global.screenHeight() / 40)

                nameSurface = self.menuFont1.render(self.gamerName, True, Colors.BLACK)
                pygame.draw.rect(Global.screen, Colors.WHITE, self.inputRect)
                Global.screen.blit(nameSurface, (self.inputRect.x + 5, self.inputRect.y + 5))

                self.inputRect.w = max(100, nameSurface.get_width() + 10)
                self.inputRect.x = Global.screenWidth() / 2 - self.inputRect.w / 2

            else:
                self.getSurfaceText(self.titleFont, 'TheGame', Colors.getRandom(), Global.screenHeight() / 4)
                self.getSurfaceText(self.menuFont1, 'Controls:', Colors.GRAY, 14 * Global.screenHeight() / 40)
                self.getSurfaceText(self.menuFont2, 'Arrows LEFT/RIGHT - Move Left/Right', Colors.WHITE,
                                    16 * Global.screenHeight() / 40)
                self.getSurfaceText(self.menuFont2, 'Arrow UP - Jump', Colors.WHITE, 17 * Global.screenHeight() / 40)
                self.getSurfaceText(self.menuFont2, 'Left SHIFT/ Left ALT/ S - Shoot', Colors.WHITE, 18 * Global.screenHeight() / 40)
                self.getSurfaceText(self.menuFont2, 'P - Pause', Colors.WHITE, 19 * Global.screenHeight() / 40)
                self.getSurfaceText(self.menuFont2, 'M - exit in Menu', Colors.WHITE,
                                    20 * Global.screenHeight() / 40)
                if self.blink:
                    self.getSurfaceText(self.menuFont1, 'Push ENTER to start', Colors.RED,
                                        22 * Global.screenHeight() / 40)
                if len(self.scoreTable) != 0:
                    self.getSurfaceText(self.menuFont1, 'High score table:', Colors.GRAY,
                                        24 * Global.screenHeight() / 40)

                for index, (name, score) in enumerate(self.scoreTable.items()):
                    self.getSurfaceText(self.menuFont2, f'{index + 1}) {name} - {score}', Colors.WHITE,
                                        (26 + index) * Global.screenHeight() / 40)

        else:
            if Global.pause:
                self.getSurfaceText(self.menuFont1, 'Pause', Colors.WHITE, 16 * Global.screenHeight() / 40)
                if self.blink:
                    self.getSurfaceText(self.menuFont1, 'Push P for continue', Colors.BLUE, 18 * Global.screenHeight() / 40)
                self.getSurfaceText(self.menuFont1, 'Push M for exit in Menu', Colors.RED, 20 * Global.screenHeight() / 40)

            self.getSurfaceText(self.gameFont, f'Scores: {Global.hero.score}', Colors.YELLOW, 0, zeroX=True)
            if Global.hero.health > 30 or self.blink:
                self.getSurfaceText(self.gameFont, f'Health: {Global.hero.health}', Colors.GREEN, 30, zeroX=True)
            if Global.hero.bullets > 50 or self.blink:
                self.getSurfaceText(self.gameFont, f'Bullets: {Global.hero.bullets}', Colors.BLUE, 60, zeroX=True)
            self.getSurfaceText(self.gameFont,
                                f'Level: {Global.difficult} ({int((Global.levelCreator.difficultPeriod - Global.levelCreator.curDifficultTime) / 60)})',
                                Colors.RED, Global.screenHeight() - 30, zeroX=True)
