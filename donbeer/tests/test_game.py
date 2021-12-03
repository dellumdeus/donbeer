from donbeer.beer import Beer
from donbeer.configuration import Configuration
from donbeer.donut import Donut
from donbeer.game import Game
from pkg_resources import NullProvider, resource_stream, resource_filename
import pytest
from unittest.mock import MagicMock, patch

beer = MagicMock()
donut = MagicMock()
game = object


def create_game():
    game = Game(MagicMock(), 60)
    return game

# @pytest.mark.parametrize("game", create_game())


def test_new_round():
    game = create_game()
    old_game_round = game.round
    game.new_round(beer)

    assert game.round == old_game_round + 1
    assert game.ran_num and game.random_time != None
    assert beer.clicks == 0


def test_get_status_when_number_is_matched():
    game = create_game()
    beer.clicks = game.ran_num
    status = game.get_status(beer)

    assert game.donut_wait_start != None
    assert status == 'donut'


def test_get_status_when_number_is_unmatched():
    game = create_game()
    game.wait = MagicMock(return_value=True)
    status = game.get_status(beer)

    assert status == 'donut'


def test_get_status_when_number_is_none():
    game = create_game()
    status = game.get_status(beer)
    assert status == 'beer'
