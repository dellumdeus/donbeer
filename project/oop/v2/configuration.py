import pygame


class Configuration:
    def __init__(self, width, height, color):
        self.window_width = width
        self.window_height = height
        self.fps_clock = pygame.time.Clock()
        self.color = color
        self.window = None

    def set_up(self, is_full_screen):
        pygame.init()
        if is_full_screen:
            self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.window = pygame.display.set_mode((self.window_width, self.window_height), 0, 32)

        self.window.fill(self.color)
