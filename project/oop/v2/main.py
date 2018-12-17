from threading import Thread
import pygame

from project.oop.v2.beer import Beer
from project.oop.v2.configuration import Configuration
from project.oop.v2.donut import Donut
from project.oop.v2.game import Game
from project.oop.v2.text import Text

FPS = 60
LIGHTBLUE = (131, 66, 244)
CYAN = (0, 255, 255)


def main():
    # Configure and create main-elements
    beer = Beer('../../images/bier2.png')
    donut = Donut(0, '../../images/donut2.png')
    print('ich werde ausgefuhrt')
    game = Game(Configuration(700, 600, LIGHTBLUE), 60)
    game.config.set_up(True)

    for element in [donut, beer]:
        element.get_rect().center = (game.config.window.get_width() / 2, game.config.window.get_height() / 2)

    game.new_round(beer)

    setup_texts(game)

    # while (game.run() not 0):

    thread = Thread(target=game.countdown)
    thread.start()
    while True:  # main game loop

        # Set the data for Points and Countdown
        game.input()
        game.event_handling(beer, donut, game.get_text('restart'))

        game.config.window.fill(LIGHTBLUE)

        if game.is_finished:
            game.show_text('result', game.points)
            game.show_text('restart')

        else:
            if game.get_status(beer) == 1:
                game.show_game_object(donut)

            else:
                game.show_game_object(beer)

            game.show_text('points', game.points)
            game.show_text('time', game.game_time)
            game.show_text('instruction')

            pygame.display.update()
            game.config.fps_clock.tick(FPS)


def setup_texts(game):
    game.add_text(Text('points', '../../fonts/MeathFLF.ttf', 50, 'Points: '))
    game.add_text(Text('time', '../../fonts/MeathFLF.ttf', 60, 'Time: '))
    game.add_text(Text('instruction', '../../fonts/MeathFLF.ttf', 50, 'Don\'t press the donut!'))
    game.add_text(Text('result', '../../fonts/MeathFLF.ttf', 80, 'Total result: '))
    game.add_text(Text('restart', '../../fonts/MeathFLF.ttf', 80, 'Restart'))
    set_text_coords(game)


def set_text_coords(game):
    game.get_text('points').set_coords(
        game.config.window.get_width() / 5,
        game.config.window.get_height() / 3
    )
    game.get_text('time').set_coords(
        game.config.window.get_width() / 4 * 3,
        game.config.window.get_height() / 3
    )
    instruction = game.get_text('instruction')
    instruction.set_coords(
        game.config.window.get_width() / 2 - instruction.label.get_width() / 2,
        game.config.window.get_height() / 4)
    game.get_text('restart').set_coords(
        game.config.window.get_width() / 2 - instruction.label.get_width() / 2,
        game.config.window.get_height() / 3 * 1.5)


if __name__ == '__main__':
    while main() == 0:
        main()
