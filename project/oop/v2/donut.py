import pygame


class Donut:

    def __init__(self, time, source):
        self.time = time
        self.source = source
        self.img = pygame.image.load(source)
        self.rect = self.img.get_rect()

    def get_image(self):
        return self.img

    def get_rect(self):
        return self.rect
