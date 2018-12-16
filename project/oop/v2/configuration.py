import pygame


class Configuration:
    def __init__(self, width, height):
        self.window_width = width
        self.window_height = height
        self.fps_clock = pygame.time.Clock()

    def set_up(self, color, is_full_screen):
        self.color = color
        pygame.init()
        if is_full_screen:
            self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.window = pygame.display.set_mode(
                (self.window_width, self.window_height), 0, 32)
        self.window.fill(self.color)