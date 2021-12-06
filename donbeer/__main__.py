from threading import Thread
from donbeer.game_config import FPS, LIGHTBLUE, TEXT_INFOS
from donbeer.objects import Beer, Donut
import pygame

from donbeer.configuration import Configuration
from donbeer.game import Game
from donbeer.helpers import SetupHelper
from pkg_resources import resource_stream


def main():
    """Run the game and create/configure main-elements"""

    beer = Beer(resource_stream(__name__, 'resources/images/beer2.png'))
    donut = Donut(0, resource_stream(__name__, 'resources/images/donut2.png'))
    game = Game(Configuration(700, 600, LIGHTBLUE), 60)
    game.config.set_up(True)
    setup_helper = SetupHelper(game, TEXT_INFOS)

    for element in [donut, beer]:
        element.rect.center = (
            game.config.window.get_width() / 2,
            game.config.window.get_height() / 2
        )

    game.new_round(beer)
    setup_helper.build_text_objs()

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


if __name__ == '__main__':
    while main() == 0:
        main()
