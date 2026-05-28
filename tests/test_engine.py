import pytest
from game.engine import Engine
from game.pacman import Pacman
from inspiration.levelmap import LevelMap
def test_engine_running():
    engine = Engine()
    assert engine.running == False


def test_engine_level_completion():

    engine = Engine()

    engine.cheese_list = []

    engine.if_win()

    assert engine.level == 2

def test_engine_game_over():

    engine = Engine()
    pacman = Pacman()

    engine.pacman.lives = 0

    engine.if_game_over()

    assert engine.game_over is True

def test_engine_game_over_lives_over_zero_bug():
    engine = Engine()
    engine.pacman.lives = 1

    result = engine.if_game_over()

    assert result is False


def test_engine_number_of_players():
    engine = Engine()

    assert engine.number_of_players == 1

def test_game_status():
    engine = Engine()

    assert engine.game_status() == "Not started"

def test_engine_pauze():
    engine = Engine()
    if engine.running:
        engine.pauze()

    assert engine.running == False



def test_engine_resume():

    engine = Engine()

    engine.game_over = False
    engine.running = False
    engine.paused = True

    engine.resume()

    assert engine.running is True
    assert engine.paused is False
def test_engine_resume_cant_resume_if_game_over_bug():
    engine = Engine()
    engine.paused = True
    engine.game_over = True
    engine.running = False

    engine.resume()

    assert engine.running is False
    assert engine.paused is True

def test_engine_restart():
    engine = Engine()

    # simulatie van inspiration over situatie
    engine.running = False
    engine.level = 3
    engine.pacman.lives = 0
    engine.game_over = True

    engine.restart()

    assert engine.running is True
    assert engine.level == 1
    assert engine.pacman.lives == 3
    assert engine.game_over is False

def test_engine_restart_resets_game_over():
    engine = Engine()
    engine.game_over = True

    engine.restart()

    assert engine.game_over is False
def test_engine_draw_map(mocker):
    engine = Engine()
    fake_map = mocker.Mock()

    engine.draw_map(fake_map)

    assert fake_map.get_tile.called

def test_engine_draw_map_level_2():
    engine = Engine(level=1)

    # alle kaas op
    engine.cheese.quantity = 0

    engine.check_level_completion()

    assert engine.level == 2
    assert engine.cheese.quantity > 0

def test_engine_stop():
    engine = Engine()

    engine.stop()

    assert engine.running == False

def test_engine_stop_already_stopped():
    engine = Engine()
    engine.running = False

    engine.stop()

    assert engine.running == False

