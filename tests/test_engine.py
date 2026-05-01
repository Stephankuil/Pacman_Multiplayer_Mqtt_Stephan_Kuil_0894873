import pytest
from game.engine import Engine
def test_engine_running():
    engine = Engine()
    assert engine.running == False


def test_engine_level_completion():
    engine = Engine()

    engine.cheese.quantity = 0

    engine.check_level_completion()

    assert engine.level == 2

def test_engine_game_over():
    pass

def test_engine_game_over_unhappy_path():
    pass

def test_engine_number_of_players():
    pass

def test_game_status():
    pass

def test_engine_pauze():
    pass

def test_engine_unpauze():
    pass


def test_engine_resume():
    pass

def test_engine_resume_unhappy_path():
    pass

def test_engine_restart():
    pass

def test_engine_restart_unhappy_path():
    pass
def test_engine_draw_map():
    pass

def test_engine_draw_map_unhappy_path():
    pass

def test_engine_stop():
    pass

def test_engine_stop_unhappy_path():
    pass

