import pygame


class Text:
    def __init__(self, font, size, content):
        # pygame.font.init()
        self.font = font  # font_path = "./fonts/newfont.ttf"
        self.fontSize = size  # font_size = 32
        self.content = content  # 'ich will essen'
        self.label = self.get_font().render(content, 1, (255, 255, 0))
        self.rect = self.label.get_rect(topleft=(788, 587))

    def get_font(self):
        return pygame.font.Font(self.font, self.fontSize)

    def get_rect(self):
        return self.rect
