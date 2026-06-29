import pygame

from code.const import *


class Score:

    def __init__(self, window):

        self.window = window

        self.background = pygame.image.load(SCORE_BG).convert()

        self.background = pygame.transform.scale(
            self.background,
            (WIN_WIDTH, WIN_HEIGHT)
        )

        self.font = pygame.font.SysFont(FONT_NAME, 30)
        self.parabens = pygame.font.SysFont(FONT_NAME, 40)

    def run(self):

        while True:

            self.window.blit(self.background, (0, 0))

            text = self.font.render(
                "ENTER - VOLTA AO MENU | ESC - SAIR",
                True,
                WHITE
            )

            self.window.blit(text, (165, 450))

            text = self.parabens.render(
                "PARABÉNS!!! VOCÊ DERROTOU O SONIC!",
                True,
                WHITE
            )

            self.window.blit(text, (90, 180))

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return SAIR

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        return MENU

                    if event.key == pygame.K_ESCAPE:
                        return SAIR