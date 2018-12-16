import datetime
import sys
from random import randint
from time import sleep

import pygame
from pygame.locals import *


class Game:
    def __init__(self, data, conf, game_time):
        self.round = 0
        self.points = 0
        self.data = data
        self.conf = conf
        self.start_time_pause = None
        self.is_finished = False
        self.game_time = game_time

    # new Round has new random Int and Local time of the pause(wait bcs of
    # Donut)
    def new_round(self, beer):
        self.round += 1
        self.ran_num = randint(2, 20)

        beer.clicks = 0
        self.random_time = randint(1, 5)

    """
    returns true if the pause is over
    """

    def wait(self):
        if self.start_time_pause is not None:
            # Adds seconds to the starttime and gets the end time
            end_time_pause = add_secs(self.start_time_pause, self.random_time)
            local_time = datetime.datetime.now().time()
            print(self.start_time_pause)
            print(end_time_pause, datetime.datetime.now().time())
            if local_time >= end_time_pause:
                self.start_time_pause = None
                return False
            else:
                return True
                """
    1 for Donut, 0 for Beer
    """

    def get_status(self, beer, donut):
        # print (beer.clicks == self.getRanNum())
        if beer.clicks == self.get_ran_num():
            self.start_time_pause = datetime.datetime.now().time()
            # print (self.start_time_pause)
            self.new_round(beer)
            return 1
        if self.wait():
            return 1
        else:
            return 0

    def get_data(self, index):
        self.data[index]

    """
    Handles the clicks of the user to the beer and donut
    """

    def event_handling(self, beer, donut, restart):
        if self.mousePos is not None:
            # if the user clicked onto beer or donut
            if self.isOverRect(
                    beer, self.mousePos) or self.isOverRect(
                donut, self.mousePos):
                # if he has clicked in the beer phase
                if self.get_status(beer, donut) == 0:
                    beer.clicks += 1
                    self.points += beer.clicks
                else:
                    self.is_finished = True
            # if the user clicked onto the restart text
            if restart.label is not None and self.isOverRect(
                    restart, self.mousePos):
                self.is_finished = False

    def input(self):
        self.mousePos = None
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # If clicked
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                self.mousePos = pygame.mouse.get_pos()

    '''
    def run(self, beer, donut):
        thread = Thread(target = game.countdown)
    thread.start()
    '''

    def show_text(self, text, xCoord, yCoord):
        # render text
        label = text.get_font().render(text.content, 1, (255, 255, 0))
        self.conf.window.blit(label, (xCoord, yCoord))

        return label

    def show_object(self, object):
        self.conf.window.fill(self.conf.color)
        self.conf.window.blit(object.get_image(), object.get_rect())
        # print (object.source)

    def isOverRect(self, object, mouse_pos):
        if object.get_rect().collidepoint(mouse_pos):
            return True
        return False

    def get_ran_num(self):
        return self.ran_num

    def get_points(self):
        return self.points

    def countdown(self):
        while self.game_time >= 0:
            # print(t)
            sleep(1)
            self.game_time -= 1
        self.is_finished = True


def add_secs(tm, secs):
    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + datetime.timedelta(seconds=secs)
    return fulldate.time()
