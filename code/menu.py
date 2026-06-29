import pygame

from code.const import *


class Menu:

    def __init__(self, window):

        self.window = window

        self.options = MENU_OPTION

        self.selected = 0

        self.background = pygame.image.load(MENU_BG).convert()

        self.background = pygame.transform.scale(
            self.background,
            (WIN_WIDTH, WIN_HEIGHT)
        )

        self.title_font = pygame.font.SysFont(FONT_NAME, 60)

        self.option_font = pygame.font.SysFont(FONT_NAME, 40)

        self.controller_font = pygame.font.SysFont(FONT_NAME, 30)


    def draw(self):

        self.window.blit(self.background, (0, 0))

        title = self.title_font.render(
            "MARIO VS SONIC",
            True,
            BLUE
        )

        self.window.blit(title, (230, 70))


        for i, option in enumerate(self.options):

            color = BLUE if i == self.selected else BLACK

            text = self.option_font.render(
                option,
                True,
                color
            )

            self.window.blit(
                text,
                (410, 210 + i * 60)
            )

        text2 = self.controller_font.render(
            "SETINHAS OU WASD - MOVIMENTO | ESPAÇO - PULO",
            True,
            BLACK
        )

        self.window.blit(
            text2,
            (110, 350 + i * 90)
        )


        pygame.display.flip()


    def run(self):

        while True:

            self.draw()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return SAIR


                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:

                        self.selected = (self.selected - 1) % len(self.options)

                    elif event.key == pygame.K_DOWN:

                        self.selected = (self.selected + 1) % len(self.options)

                    elif event.key == pygame.K_RETURN:

                        if self.selected == 0:
                            return NIVEL

                        return SAIR