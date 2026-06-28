import pygame

from code.const import NIVEL_BG, WIN_WIDTH, WIN_HEIGHT


class Background:

    def __init__(self):

        self.image = pygame.image.load(NIVEL_BG).convert()

        self.image = pygame.transform.scale(
            self.image,
            (WIN_WIDTH, WIN_HEIGHT)
        )

    def draw(self, window):
        window.blit(self.image, (0, 0))