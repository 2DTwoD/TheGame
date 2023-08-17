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

        self.keyBounce = False
        self.blink = True
        self.blinkCount = 0

        try:
            file = open("scores.txt", "r", encoding='UTF-8')
            for line in file:
                name, score = line.split(" ")
                score = int(score.removesuffix('\n'))
                self.scoreTable[name] = score
            file.close()
        except Exception as ex:
            print(ex)

    def inputTextHandler(self, event):
        if self.newScore and Global.gameOver:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.gamerName = self.gamerName[:-1]
                elif event.key != pygame.K_RETURN:
                    if len(self.gamerName) < 30:
                        self.gamerName += event.unicode

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
                self.getSurfaceText(self.menuFont1, f'Your scores: {Global.levelCreator.score}', Colors.BLUE,
                                    16 * Global.screenHeight() / 40)
                self.getSurfaceText(self.menuFont1, 'Enter your name:', self.color,
                                    18 * Global.screenHeight() / 40)

                nameSurface = self.menuFont1.render(self.gamerName, True, Colors.BLACK)
                pygame.draw.rect(Global.screen, Colors.WHITE, self.inputRect)
                Global.screen.blit(nameSurface, (self.inputRect.x + 5, self.inputRect.y + 5))

                self.inputRect.w = max(100, nameSurface.get_width() + 10)
                self.inputRect.x = Global.screenWidth() / 2 - self.inputRect.w / 2

                if Global.keys[pygame.K_RETURN]:
                    if self.gamerName.strip() == '':
                        self.gamerName = 'Anonymous'
                    if self.gamerName in self.scoreTable:
                        if Global.levelCreator.score > self.scoreTable[self.gamerName]:
                            self.scoreTable[self.gamerName] = Global.levelCreator.score
                    else:
                        self.scoreTable[self.gamerName] = Global.levelCreator.score
                    self.scoreTable = dict(sorted(self.scoreTable.items(), key=lambda item: item[1], reverse=True))
                    self.scoreTable = dict(itertools.islice(self.scoreTable.items(), 10))
                    with open("scores.txt", "a") as file:
                        file.truncate(0)
                        for name, score in self.scoreTable.items():
                            file.write(f'{name} {score}\n')
                    self.newScore = False
                    self.keyBounce = True

            else:
                self.getSurfaceText(self.titleFont, 'TheGame', Colors.getRandom(), 3 * Global.screenHeight() / 10)
                self.getSurfaceText(self.menuFont1, 'Controls:', Colors.GRAY, 16 * Global.screenHeight() / 40)
                self.getSurfaceText(self.menuFont2, 'A/D - Left/Right', Colors.WHITE,
                                    18 * Global.screenHeight() / 40)
                self.getSurfaceText(self.menuFont2, 'W - Jump', Colors.WHITE, 19 * Global.screenHeight() / 40)
                self.getSurfaceText(self.menuFont2, 'SPACE - Shoot', Colors.WHITE, 20 * Global.screenHeight() / 40)
                if self.blink:
                    self.getSurfaceText(self.menuFont1, 'Push ENTER to start', Colors.RED,
                                        22 * Global.screenHeight() / 40)
                if len(self.scoreTable) != 0:
                    self.getSurfaceText(self.menuFont1, 'High score table:', Colors.GRAY,
                                        24 * Global.screenHeight() / 40)

                for index, (name, score) in enumerate(self.scoreTable.items()):
                    self.getSurfaceText(self.menuFont2, f'{index + 1}) {name} - {score}', Colors.WHITE,
                                        (26 + index) * Global.screenHeight() / 40)

                if Global.keys[pygame.K_RETURN] and Global.setsIsEmpty() and not self.keyBounce:
                    Global.gameOver = False
                    Global.hero.reInit()
                    Global.levelCreator.reInit()
                    self.newScore = True
                if not Global.keys[pygame.K_RETURN]:
                    self.keyBounce = False
        else:
            self.getSurfaceText(self.gameFont, f'Scores: {Global.levelCreator.score}', Colors.YELLOW, 0, zeroX=True)
            if Global.hero.health > 20 or self.blink:
                self.getSurfaceText(self.gameFont, f'Health: {Global.hero.health}', Colors.RED, 30, zeroX=True)
            if Global.hero.bullets > 30 or self.blink:
                self.getSurfaceText(self.gameFont, f'Bullets: {Global.hero.bullets}', Colors.BLUE, 60, zeroX=True)
