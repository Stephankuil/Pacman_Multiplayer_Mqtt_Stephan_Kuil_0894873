import pytest
from game.ghosts import Ghost
from game.pacman import Pacman
from inspiration.levelmap import LevelMap
def test_ghosts():
    ghost = Ghost(
        color="red",
        x_coordinate=0,
        y_coordinate=0,

    )

    assert ghost.color == "red"
    assert ghost.x_coordinate == 0
    assert ghost.y_coordinate == 0
    assert ghost.edible is False


def test_color():
    ghost = Ghost(color="red", x_coordinate=0, y_coordinate=0)
    assert ghost.color == "red"


def test_edible():
    ghost = Ghost(color="red", x_coordinate=0, y_coordinate=0)
    assert not ghost.edible

def test_make_edible():
    ghost = Ghost(color="red", x_coordinate=0, y_coordinate=0)
    ghost.make_edible(duration=10)
    assert ghost.edible


def test_edible_timer():
    ghost = Ghost(color="red", x_coordinate=0, y_coordinate=0)

    ghost.make_edible(duration=10)

    assert ghost.edible

    # Simuleer tijd
    ghost.update_edible_timer(10)

    assert not ghost.edible

def test_make_inedible():
    ghost = Ghost(color="red", x_coordinate=0, y_coordinate=0)
    ghost.make_edible(duration=10)
    assert ghost.edible
    ghost.make_normal()
    assert not ghost.edible

def test_make_inedible_unhappy_path():
    ghost = Ghost(color="red", x_coordinate=0, y_coordinate=0)
    ghost.make_normal()  # Should not raise an error even if already inedible
    assert not ghost.edible
    ghost.make_normal()  # Should still not raise an error
    assert not ghost.edible

def test_hit_pacman():
    ghost = Ghost(
        color="red",
        x_coordinate=0,
        y_coordinate=0
    )

    pacman = Pacman()

    ghost.hit_pacman(pacman)

    assert pacman.lives == 2

def test_ghost_eat_pacman():
    ghost = Ghost(color="red", x_coordinate=0, y_coordinate=0)
    pacman = Pacman()
    if ghost.hit_pacman(pacman):
        result = "Pacman eaten"
        pacman.lose_life()
        assert pacman.lives == 2

def test_wall_check():

    game_map = LevelMap(
        [
            "000",
            "010",
            "000"
        ],
        width=3,
        height=3,
        number_of_maps=1
    )

    ghost = Ghost(
        color="red",
        x_coordinate=0,
        y_coordinate=0
    )

    assert ghost.wall_check((0, 0), game_map) is True
    assert ghost.wall_check((1, 1), game_map) is False
    assert ghost.wall_check((-1, 0), game_map) is False


def test_wall_check_out_of_bounds():
    ghost = Ghost(color="red", x_coordinate=0, y_coordinate=0)
    game_map = LevelMap(
        [
            "000",
            "010",
            "000"
        ],
        width=3,
        height=3,
        number_of_maps=1
    )
    assert ghost.wall_check((1000, 1000), game_map) is False  # Assuming (100, 100) is out of bounds


