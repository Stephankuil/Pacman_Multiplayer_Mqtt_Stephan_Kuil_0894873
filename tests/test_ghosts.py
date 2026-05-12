import pytest
from inspiration.ghosts import Ghost
from inspiration.pacman import Pacman

def test_ghosts():
    ghost = Ghost(color="red", starting_position=(0, 0))
    assert ghost

def test_color():
    ghost = Ghost(color="red", starting_position=(0, 0))
    assert ghost.color == "red"


def test_edible():
    ghost = Ghost(color="red", starting_position=(0, 0))
    assert not ghost.edible

def test_make_edible():
    ghost = Ghost(color="red", starting_position=(0, 0))
    ghost.make_edible(duration=10)
    assert ghost.edible


def test_edible_timer():
    ghost = Ghost(color="red", starting_position=(0, 0))
    ghost.make_edible(duration=10)
    assert ghost.edible
    # Simulate time passing
    ghost.update_edible_timer(10)
    #make a timer -1 to simulate the timer running out while ghost edible is true.

    assert not ghost.edible



def test_make_inedible():
    ghost = Ghost(color="red", starting_position=(0, 0))
    ghost.make_edible(duration=10)
    assert ghost.edible
    ghost.make_inedible()
    assert not ghost.edible

def test_make_inedible_unhappy_path():
    ghost = Ghost(color="red", starting_position=(0, 0))
    ghost.make_inedible()  # Should not raise an error even if already inedible
    assert not ghost.edible
    ghost.make_inedible()  # Should still not raise an error
    assert not ghost.edible

def test_hit_pacman():
    ghost = Ghost(color="red", starting_position=(0, 0))
    assert not ghost.hit_pacman()  # Should return False when inedible
    ghost.make_edible(duration=10)
    assert ghost.hit_pacman()  # Should return True when edible

def test_hit_pacman():
    ghost = Ghost(color="red", starting_position=(0, 0))
    assert not ghost.hit_pacman()  # Should return False when inedible
    ghost.make_edible(duration=10)
    assert ghost.hit_pacman()  # Should return True when edible

def test_ghost_eat_pacman():
    ghost = Ghost(color="red", starting_position=(0, 0))
    pacman = Pacman(starting_position=(0, 0))
    if ghost.hit_pacman():
        result = "Pacman eaten"
        pacman.lose_life()
        assert pacman.lives == 2

def test_wall_check():
    ghost = Ghost(color="red", starting_position=(0, 0))
    assert ghost.wall_check((1, 0)) == True  # Assuming (1, 0) is a valid position
    assert ghost.wall_check((-1, 0)) == False  # Assuming (-1, 0) is a wall

def test_wall_check_out_of_bounds():
    ghost = Ghost(color="red", starting_position=(0, 0))
    assert ghost.wall_check((1000, 1000)) == False  # Assuming (100, 100) is out of bounds


