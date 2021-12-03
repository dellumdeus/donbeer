from donbeer.game import Game
from unittest.mock import MagicMock
import pytest

beer = MagicMock()
donut = MagicMock()


@pytest.fixture(autouse=True)
def game():
    return Game(MagicMock(), 60)


def test_new_round(game):
    old_game_round = game.round
    game.new_round(beer)

    assert game.round == old_game_round + 1
    assert game.ran_num and game.random_time != None
    assert beer.clicks == 0


def test_get_status_when_waiting_starts(game):
    beer.clicks = game.ran_num
    status = game.get_status(beer)

    assert game.donut_wait_start != None
    assert status == 'donut'


def test_get_status_when_waiting(game):
    game.wait = MagicMock(return_value=True)
    status = game.get_status(beer)

    assert status == 'donut'


def test_get_status_when_waiting_is_over(game):
    status = game.get_status(beer)
    assert status == 'beer'
