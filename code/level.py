import pygame

from code.const import *
from code.entitymediator import EntityMediator
from code.entityfactory import EntityFactory


class Level:

    def __init__(self, window):

        self.window = window

        self.background = EntityFactory.get_entity("Background")
        self.player = EntityFactory.get_entity("Player")
        self.enemy = EntityFactory.get_entity("Enemy")

    def draw(self):

        self.background.draw(self.window)

        self.player.draw(self.window)

        if self.enemy.alive:
            self.enemy.draw(self.window)

        pygame.display.flip()

    def run(self):

        clock = pygame.time.Clock()

        while True:

            self.player.update()
            self.enemy.update()

            state = EntityMediator.verify(
                self.player,
                self.enemy
            )

            if state != NIVEL:
                return state

            self.draw()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return SAIR

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        return MENU

            clock.tick(FPS)