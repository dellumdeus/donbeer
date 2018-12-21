import pygame


class Text:
    def __init__(self, name, font, size, content=""):
        # pygame.font.init()
        self.name = name
        self.x = 0
        self.y = 0
        self.font = font  # font_path = "./fonts/newfont.ttf"
        self.fontSize = size  # font_size = 32
        self.content = [content, 0]
        self.label = self.get_font().render(content, 1, (255, 255, 0))
        self.rect = None

    def get_font(self):
        return pygame.font.Font(self.font, self.fontSize)

    def get_rect(self):
        return self.label.get_rect(topleft=(self.x, self.y))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def set_label(self, with_var):
        if with_var:
            self.label = self.get_font().render(self.content[0] + str(self.content[1]), 1, (255, 255, 0))
        else:
            self.label = self.get_font().render(self.content[0], 1, (255, 255, 0))
