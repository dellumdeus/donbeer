from threading import Thread
import pygame

from donbeer.beer import Beer
from donbeer.configuration import Configuration
from donbeer.donut import Donut
from donbeer.game import Game
from donbeer.text import Text
from donbeer.helpers import build_text_objs, set_text_coords
from pkg_resources import resource_stream

FPS = 60
LIGHTBLUE = (131, 66, 244)
CYAN = (0, 255, 255)

TEXT_DICT = {
    "basic": {"points", "time", "round"},
    "instruction": ['Don\'t press the donut!', 60],
    "result": ['Total result: ', 130],
    "restart": ['>>>RESTART<<<', 80]
}


def main():
    """Run the game and create/configure main-elements"""

    beer = Beer(resource_stream(__name__, 'resources/images/beer2.png'))
    donut = Donut(0, resource_stream(__name__, 'resources/images/donut2.png'))
    game = Game(Configuration(700, 600, LIGHTBLUE), 60)
    game.config.set_up(True)

    for element in [donut, beer]:
        element.rect.center = (
            game.config.window.get_width() / 2,
            game.config.window.get_height() / 2
        )

    game.new_round(beer)

    setup_texts(game)

    thread = Thread(target=game.countdown)
    thread.start()
    while True:  # main game loop
        # Set the data for Points and Countdown
        game.handle_input()
        game.handle_event(beer, donut)

        game.config.window.fill(LIGHTBLUE)
        if game.new_game:
            break

        if game.is_finished:
            game.show_text('result', game.points)
            game.show_text('restart')

        else:
            if game.get_status(beer) == 'donut':
                game.show_game_object(donut)

            else:
                game.show_game_object(beer)

            game.show_text('points', game.points)
            game.show_text('round', game.round)
            game.show_text('time', game.game_time)
            game.show_text('instruction')

        pygame.display.update()
        game.config.fps_clock.tick(FPS)
    return 0


def setup_texts(game):
    build_text_objs(game, TEXT_DICT)
    set_text_coords(game, 'points')
    set_text_coords(game, 'round', {'h': 7})
    set_text_coords(game, 'time', {'w': 7.5})

    set_text_coords(game, 'instruction', {'h': 2, 'w': 5})
    set_text_coords(game, 'result', {'h': 3, 'w': 5})
    set_text_coords(game, 'restart', {'h': 7, 'w': 5})


if __name__ == '__main__':
    while main() == 0:
        main()
