import pygame, sys, random, datetime, time, multiprocessing, threading
from pygame.locals import *
from random import randint
from time import sleep
from multiprocessing import Process
from threading import Thread

FPS = 60
LIGHTBLUE =(131,  66, 244)
CYAN     = (  0, 255, 255)
def addSecs(tm, secs):
    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + datetime.timedelta(seconds=secs)
    return fulldate.time()

class Beer:

    def __init__(self, source):
        self.clicks = 0
        self.source = source
        self.img = pygame.image.load(source)
        self.rect = self.img.get_rect()

    def getImage(self):
        return self.img
    
    def getRect(self):
        return self.rect
    
class Donut:

    def __init__(self, time, source):
        self.time = time
        self.source = source
        self.img = pygame.image.load(source)
        self.rect = self.img.get_rect()

        
    def getImage(self):
        return self.img
    
    def getRect(self):
        return self.rect
        
def tester(beer, beerRect):
    print (beer.getRect().centerx)
    print (beer.getRect().centery)

class Configuration:
    def __init__(self, width, height):
        self.windowWidth = width
        self.windowHeight = height
        self.fpsClock = pygame.time.Clock()

    def setUp(self, color, isFullScreen):
        self.color = color
        pygame.init()
        if (isFullScreen):
            self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight), 0, 32)
        self.window.fill(self.color)
        
class Text:
    def __init__(self, font, size, content):
        #pygame.font.init()
        self.font = font #font_path = "./fonts/newfont.ttf"
        self.fontSize = size #font_size = 32
        self.content = content #'ich will essen'

    def getFont(self):
         return pygame.font.Font(self.font, self.fontSize)

class Game:
    def __init__(self, data, conf, gameTime):
        self.round = 0
        self.points = 0
        self.data = data
        self.conf = conf
        self.startTimePause = None
        self.isFinished = False
        self.gameTime = gameTime
    
    #new Round has new random Int and Local time of the pause(wait bcs of Donut)     
    def newRound(self, beer):
        self.round += 1
        self.ranNum = randint(2, 20)
        
        beer.clicks = 0
        self.randomTime = randint(1, 5)

    """
    returns true if the pause is over
    """
    def wait(self, beer):
        #print (self.startTimePause)
        if (self.startTimePause != None):
            #Adds seconds to the starttime and gets the end time
            endTimePause = addSecs(self.startTimePause, self.randomTime)
            localTime = datetime.datetime.now().time()
            print (self.startTimePause)
            print (endTimePause, datetime.datetime.now().time())
            if(localTime >= endTimePause):
                self.startTimePause = None
                return False
            else:
                return True
                """
    1 for Donut, 0 for Beer
    """
    def getStatus(self, beer, donut):
        #print (beer.clicks == self.getRanNum())
        if (data[0].clicks == self.getRanNum()):
            self.startTimePause = datetime.datetime.now().time()
            #print (self.startTimePause)
            self.newRound(beer)
            return 1
        if(self.wait(beer)):
            return 1
        else:
            return 0
        
    def getData(self, index):
        self.data[index]
        
    """
    Handles the clicks of the user to the beer and donut
    """
    def eventHandling(self, beer, donut, restart):
        if (self.mousePos != None):
            #if the user clicked onto beer or donut
            if (self.isOverRect(beer, self.mousePos) or self.isOverRect(donut, self.mousePos)):
                #if he has clicked in the beer phase
                if(self.getStatus(beer, donut) == 0):
                    beer.clicks += 1
                    self.points += beer.clicks
                else:
                    self.isFinished = True
            #if (self.isOverRect(restart, self.mousePos))
        
    def input(self):
        self.mousePos = None
        for event in pygame.event.get():
            if (event.type == QUIT):
                pygame.quit()
                sys.exit()
                    
            #If clicked
            elif (event.type == MOUSEBUTTONUP and event.button == 1):
                self.mousePos = pygame.mouse.get_pos()
    '''
    def run(self, beer, donut):
        thread = Thread(target = game.countdown)
    thread.start()


    
    
    while True: # main game loop
        
        #Set the data for Points and Countdown
        pointsText.content = 'Points: ' + str(game.points)
        timeText.content = 'Time: ' + str(game.gameTime)
        instructionText.content = 'Don\'t press the donut!'
        resultText.content = 'Total result: ' + str(game.points)
        restartText.content = 'Restart'
        
        label = instructionText.getFont().render(instructionText.content, 1, (255,255,0))
        game.input()
        game.eventHandling(beer, donut)

        game.conf.window.fill(LIGHTBLUE)
        
        if (game.isFinished):
            game.showText(resultText, (game.conf.window.get_width()/2)- (label.get_width()/2), game.conf.window.get_height()/3)
            game.showText(restartText, (game.conf.window.get_width()/2)- (label.get_width()/2), (game.conf.window.get_height()/3) *1.5)
            #return 0
            
        else:
            if(game.getStatus(beer, donut) == 1):
                game.showObject(donut)
            
            else:
                game.showObject(beer)
            
            
            game.showText(pointsText, game.conf.window.get_width()/5, game.conf.window.get_height()/3)
            game.showText(timeText, (game.conf.window.get_width()/4)*3, game.conf.window.get_height()/3)
            game.showText(instructionText, (game.conf.window.get_width()/2)- (label.get_width()/2), game.conf.window.get_height()/4)

        
        
        pygame.display.update()
        game.conf.fpsClock.tick(FPS)
      '''      
    def showText(self, text, xCoord, yCoord):
        # render text
        label = text.getFont().render(text.content, 1, (255,255,0))
        self.conf.window.blit(label, (xCoord, yCoord))

        return label
        
    def showObject(self, object):
        self.conf.window.fill(self.conf.color)
        self.conf.window.blit(object.getImage(), object.getRect())
        #print (object.source)
        
    def isOverRect(self, object, mousePos):
        if (object.getRect().collidepoint(mousePos)):
            return True
        return False

    def getRanNum(self):
        return self.ranNum
    
    def getPoints(self):
        return self.points
    
    def countdown(self):
        while self.gameTime >= 0:
            #print(t)
            sleep(1)
            self.gameTime -= 1
        self.isFinished = True
        
def main():
    
    #Hauptelemente erstellen und konfigurieren
    beer = Beer('images/bier2.png')
    beerimg = beer.getImage()
    beerRect = beerimg.get_rect()
    
    donut = Donut(0,'images/donut2.png' )
    data = [beer, donut]
    
    conf = Configuration(700, 600)
    game = Game(data, conf, 60)
    game.conf.setUp(LIGHTBLUE, True)
    
    beer.getRect().center = (game.conf.window.get_width()/2, game.conf.window.get_height()/2)
    donut.getRect().center = (game.conf.window.get_width()/2, game.conf.window.get_height()/2)
    
    game.newRound(beer)
    
    pointsText = Text('fonts/MeathFLF.ttf', 50, '')
    instructionText = Text('fonts/MeathFLF.ttf', 60, '')
    timeText = Text('fonts/MeathFLF.ttf', 50, '')
    resultText = Text('fonts/MeathFLF.ttf', 80, '')
    restartText = Text('fonts/MeathFLF.ttf', 80, '')
    print (data[donut])
    '''
    while (game.run() not 0):
        
    
    thread = Thread(target = game.countdown)
    thread.start()

    
    
    while True: # main game loop
        
        #Set the data for Points and Countdown
        pointsText.content = 'Points: ' + str(game.points)
        timeText.content = 'Time: ' + str(game.gameTime)
        instructionText.content = 'Don\'t press the donut!'
        resultText.content = 'Total result: ' + str(game.points)
        restartText.content = 'Restart'
        
        label = instructionText.getFont().render(instructionText.content, 1, (255,255,0))
        game.input()
        game.eventHandling(beer, donut)

        game.conf.window.fill(LIGHTBLUE)
        
        if (game.isFinished):
            game.showText(resultText, (game.conf.window.get_width()/2)- (label.get_width()/2), game.conf.window.get_height()/3)
            game.showText(restartText, (game.conf.window.get_width()/2)- (label.get_width()/2), (game.conf.window.get_height()/3) *1.5)
            #return 0
            
        else:
            if(game.getStatus(beer, donut) == 1):
                game.showObject(donut)
            
            else:
                game.showObject(beer)
            
            
            game.showText(pointsText, game.conf.window.get_width()/5, game.conf.window.get_height()/3)
            game.showText(timeText, (game.conf.window.get_width()/4)*3, game.conf.window.get_height()/3)
            game.showText(instructionText, (game.conf.window.get_width()/2)- (label.get_width()/2), game.conf.window.get_height()/4)

        
        
        pygame.display.update()
        game.conf.fpsClock.tick(FPS)
    '''
           
if __name__ == '__main__':
        while main() == 0:
            main()
