import pygame
import sys

from code.const import *
from code.menu import Menu
from code.level import Level
from code.score import Score


class Game:

    def __init__(self):

        pygame.init()

        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        pygame.display.set_caption("Mini Mario")

        self.clock = pygame.time.Clock()

        self.state = MENU


    def run(self):

        while True:

            if self.state == MENU:

                menu = Menu(self.window)

                self.state = menu.run()

            elif self.state == NIVEL:
                level = Level(self.window)
                self.state = level.run()

            elif self.state == SCORE:
                score = Score(self.window)
                self.state = score.run()


            elif self.state == SAIR:

                pygame.quit()
                sys.exit()

            self.clock.tick(FPS)