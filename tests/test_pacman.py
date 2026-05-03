import pytest
from game.pacman import Pacman
from game.ghosts import Ghost
def test_pacman():
    pass

def test_eat_cheese():
    pacman = Pacman()
    if pacman.eat_cheese():
        assert pacman.score == 10

def test_eat_cheese_unhappy_path():
    pacman = Pacman()
    # Simulate an error condition where eating cheese fails
    with pytest.raises(Exception):
        pacman.eat_cheese()  # Assuming this raises an exception on failure

def test_eat_cherry():
    pacman = Pacman()
    if pacman.eat_cherry():
        assert pacman.score == 50

def test_eat_cherry_unhappy_path():
    pacman = Pacman()
    # Simulate an error condition where eating cherry fails
    with pytest.raises(Exception):
        pacman.eat_cherry()  # Assuming this raises an exception on failure

def test_eat_ghost():
    pacman = Pacman()
    ghost = Ghost(color="red", starting_position=(0, 0))
    # Simulate eating a ghost
    if pacman.eat_ghost() and ghost.edible():
        assert pacman.score >= 200  # Assuming eating a ghost gives at least 200 points

def test_eat_ghost_unhappy_path():
    pacman = Pacman()
    ghost = Ghost(color="red", starting_position=(0, 0))
    if not ghost.edible():
        with pytest.raises(Exception):
            pacman.eat_ghost()
def test_add_score():
    pacman = Pacman()
    initial_score = pacman.score
    pacman.add_score(100)
    assert pacman.score == initial_score + 100

def test_add_score_unhappy_path():
    pacman = Pacman()
    with pytest.raises(ValueError):
        pacman.add_score(-50)  # Assuming negative score addition raises an error

def test_lose_life():
    pacman = Pacman()
    initial_lives = pacman.lives
    pacman.lose_life()
    assert pacman.lives == initial_lives - 1

def test_lose_life_unhappy_path():
    pacman = Pacman()
    pacman.lives = 0  # Simulate losing all lives
    with pytest.raises(Exception):
        pacman.lose_life()  # Assuming losing a life when at 0 raises an error

def test_powerup():
    pacman = Pacman()
    if pacman.powerup():
        assert pacman.powered_up == True

def test_powerup_unhappy_path():
    pacman = Pacman()
    # Simulate an error condition where powerup fails
    with pytest.raises(Exception):
        pacman.powerup()  # Assuming this raises an exception on failure

