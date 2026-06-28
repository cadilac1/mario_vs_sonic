from code.entity import Entity
from code.const import *

import pygame

class Player(Entity):

    def __init__(self):

        super().__init__(
            PLAYER_IMG,
            (120, GROUND_Y),
            (64, 64)
        )

        self.speed = PLAYER_SPEED

        self.vel_y = 0

        self.on_ground = True

    def update(self):

        keys = pygame.key.get_pressed()

        # Movimento horizontal
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        # Pulo
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.on_ground:
            self.vel_y = JUMP_FORCE

            self.on_ground = False

        # Gravidade
        self.vel_y += GRAVITY

        self.rect.y += self.vel_y

        # Colisão com o chão
        if self.rect.y >= GROUND_Y:
            self.rect.y = GROUND_Y

            self.vel_y = 0

            self.on_ground = True

        # Limites da tela
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH