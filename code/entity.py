import pygame


class Entity:

    def __init__(self, image_path, position, size):

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)

        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def draw(self, window):
        window.blit(self.image, self.rect)