import datetime
import sys
from random import randint
from time import sleep

import pygame
from pygame.locals import *


class Game:
    def __init__(self, config, game_time):
        self.texts = []
        self.round = 0
        self.points = 0
        self.config = config
        self.donut_wait_start = None
        self.is_finished = False
        self.game_time = game_time
        self.ran_num = None
        self.random_time = None

    # new Round has new random Int and Local time of the pause(wait bcs of Donut)
    def new_round(self, beer):
        self.round += 1
        self.ran_num = randint(2, 20)

        beer.clicks = 0
        self.random_time = randint(1, 5)

    """
    returns true if the pause is over
    """

    def wait(self):
        if self.donut_wait_start:
            # Adds seconds to the start-time and gets the end time
            donut_wait_end = self.donut_wait_start + datetime.timedelta(seconds=self.random_time)
            if datetime.datetime.now() >= donut_wait_end:
                self.donut_wait_start = None
                return False
            else:
                return True

    """
    1 for Donut, 0 for Beer
    """

    def get_status(self, beer):
        if beer.clicks == self.get_ran_num():
            self.donut_wait_start = datetime.datetime.now()
            self.new_round(beer)
            return 1
        elif self.wait():
            return 1
        else:
            return 0

    """
    Handles the clicks of the user to the beer and donut
    """

    def event_handling(self, beer, donut, restart):
        if self.mouse_pos is not None:
            # if the user clicked onto beer or donut
            if Game.is_over_rect(beer, self.mouse_pos) or Game.is_over_rect(donut, self.mouse_pos):
                # if he has clicked in the beer phase
                if self.get_status(beer) == 0:
                    beer.clicks += 1
                    self.points += beer.clicks
                else:
                    self.is_finished = True
            # if the user clicked onto the restart text
            if Game.is_over_rect(self.get_text('restart'), self.mouse_pos):
                self.is_finished = False

    def input(self):
        self.mouse_pos = None
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # If clicked
            if event.type == MOUSEBUTTONUP and event.button == 1:
                self.mouse_pos = pygame.mouse.get_pos()

    '''
    def run(self, beer, donut):
        thread = Thread(target = game.countdown)
    thread.start()
    '''

    def show_text(self, text_name, var=None):
        text = self.get_text(text_name)
        if var:
            text.content[1] = var
            text.set_label(True)
        else:
            text.set_label(False)
        print(text.content)
        # render text
        self.config.window.blit(text.label, (text.x, text.y))
        return text.label

    def show_game_object(self, game_object):
        self.config.window.fill(self.config.color)
        self.config.window.blit(
            game_object.get_image(),
            game_object.get_rect())
        # print (object.source)

    @staticmethod
    def is_over_rect(game_object, mouse_pos):
        if game_object.get_rect().collidepoint(mouse_pos):
            return True
        return False

    def get_ran_num(self):
        return self.ran_num

    def countdown(self):
        while self.game_time >= 0:
            # print(t)
            sleep(1)
            self.game_time -= 1
        self.is_finished = True

    def add_text(self, text):
        self.texts.append(text)

    def get_text(self, text_name):
        for text in self.texts:
            if text.name == text_name:
                return text
