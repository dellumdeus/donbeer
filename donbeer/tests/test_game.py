from donbeer.game import Game
from unittest.mock import MagicMock, patch
import pytest
import pdb
import time

beer = MagicMock()
donut = MagicMock()


@pytest.fixture(autouse=True)
def game():
    return Game(MagicMock(), 60)


def test_new_round(game):
    old_game_round = game.round
    game.new_round(beer)

    assert game.round == old_game_round + 1
    assert game.ran_num and game.random_time is not None
    assert beer.clicks == 0


def test_get_status_when_waiting_starts(game):
    beer.clicks = game.ran_num
    status = game.get_status(beer)

    assert game.donut_wait_start is not None
    assert status == 'donut'


def test_get_status_when_waiting(game):
    game.wait = MagicMock(return_value=True)
    status = game.get_status(beer)

    assert status == 'donut'


def test_get_status_when_waiting_is_over(game):
    status = game.get_status(beer)
    assert status == 'beer'


@pytest.fixture(autouse=True)
def mock_texts():
    mock_texts = [MagicMock() for n in range(3)]
    for idx, item in enumerate(mock_texts):
        item.name = f"text {idx}"
    return mock_texts


def test_get_text_when_it_matches(game, mock_texts):
    game.texts = mock_texts
    assert game.get_text("text 1") == mock_texts[1]


def test_get_text_when_it_matches_not(game, mock_texts):
    game.texts = mock_texts
    assert game.get_text("text 1") != mock_texts[2]


@patch('donbeer.game.sleep', return_value=None)
def test_countdown_while_running(patched_sleep, game):
    game.game_time = 60
    game.is_finished = False
    game.countdown()
    assert patched_sleep.call_count == 61
    assert game.game_time == -1
    assert game.is_finished
