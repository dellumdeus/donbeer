

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
    data = [beer, donut]

    conf = Configuration(700, 600)
    game = Game(data, conf, 60)
    game.conf.set_up(LIGHTBLUE, True)

    beer.get_rect().center = (
        game.conf.window.get_width() / 2,
        game.conf.window.get_height() / 2)
    donut.get_rect().center = (
        game.conf.window.get_width() / 2,
        game.conf.window.get_height() / 2)

    game.new_round(beer)

    points_text = Text('../../fonts/MeathFLF.ttf', 50, '')
    instruction_text = Text('../../fonts/MeathFLF.ttf', 60, '')
    time_text = Text('../../fonts/MeathFLF.ttf', 50, '')
    result_text = Text('../../fonts/MeathFLF.ttf', 80, '')
    restart_text = Text('../../fonts/MeathFLF.ttf', 80, 'Restart')

    # while (game.run() not 0):

    thread = Thread(target=game.countdown)
    thread.start()
    while True:  # main game loop

        # Set the data for Points and Countdown
        points_text.content = 'Points: ' + str(game.points)
        time_text.content = 'Time: ' + str(game.game_time)
        instruction_text.content = 'Don\'t press the donut!'
        result_text.content = 'Total result: ' + str(game.points)

        instruction_text_label = instruction_text.get_font().render(
            instruction_text.content, 1, (255, 255, 0))
        game.input()
        game.event_handling(beer, donut, restart_text)

        game.config.window.fill(LIGHTBLUE)

        if game.is_finished:
            game.show_text(result_text, (game.config.window.get_width(
            ) / 2) - (instruction_text_label.get_width() / 2), game.config.window.get_height() / 3)
            restart_text.label = game.show_text(
                restart_text,
                (game.config.window.get_width() / 2) - (
                        instruction_text_label.get_width() / 2),
                (game.config.window.get_height() / 3) * 1.5)
            # return 0

        else:
            if game.get_status(beer, donut) == 1:
                game.show_game_object(donut)

            else:
                game.show_game_object(beer)

            game.show_text(
                points_text,
                game.config.window.get_width() / 5,
                game.config.window.get_height() / 3)
            game.show_text(
                time_text,
                (game.config.window.get_width() / 4) * 3,
                game.config.window.get_height() / 3)
            game.show_text(instruction_text, (game.config.window.get_width(
            ) / 2) - (instruction_text_label.get_width() / 2), game.config.window.get_height() / 4)

        pygame.display.update()
        game.config.fps_clock.tick(FPS)


if __name__ == '__main__':
    while main() == 0:
        main()
