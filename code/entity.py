import pygame


class Entity:

    def __init__(self, image_path, position, size):

        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.original_image = pygame.transform.scale(
            self.original_image,
            size)

        self.image = self.original_image

        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def draw(self, window):
        window.blit(self.image, self.rect)