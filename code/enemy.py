from code.entity import Entity
from code.const import *


class Enemy(Entity):

    def __init__(self):

        super().__init__(
            ENEMY_IMG,
            (700, GROUND_Y),
            (64, 64)
        )

        self.speed = ENEMY_SPEED
        self.direction = -1
        self.alive = True

    def update(self):

        if not self.alive:
            return

        self.rect.x += self.speed * self.direction

        # Limites do movimento
        if self.rect.left <= 0:
            self.direction = 1

        elif self.rect.right >= 960:
            self.direction = -1