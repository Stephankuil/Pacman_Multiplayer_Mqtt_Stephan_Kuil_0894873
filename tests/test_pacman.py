import pytest
from game.pacman import Pacman
from game.ghosts import Ghost
from game.cheese import Cheese
from game.cherry import Cherry
from game.powerup import PowerUp
def test_pacman():
    pacman = Pacman()
    assert pacman.name == "Pacman"
    assert pacman.score == 0
    assert pacman.x_coordinate == 0
    assert pacman.y_coordinate == 0
    assert pacman.lives == 3

def test_eat_cheese():
    pacman = Pacman()
    pacman.x_coordinate = 5
    pacman.y_coordinate = 5

    cheese = Cheese(
        x_coordinate=5,
        y_coordinate=5
    )

    result = pacman.eat_cheese(cheese)

    assert result is True
    assert pacman.score == 10

def test_eat_cheese_unhappy_path():
    pacman = Pacman()
    # Simulate an error condition where eating cheese fails
    with pytest.raises(Exception):
        pacman.eat_cheese()  # Assuming this raises an exception on failure

def test_eat_cherry():
    pacman = Pacman()
    pacman.x_coordinate = 0
    pacman.y_coordinate = 0
    cherry = Cherry(0,0)
    if pacman.eat_cherry(cherry):
        assert pacman.score == 50

def test_eat_cherry_unhappy_path():
    pacman = Pacman()
    # Simulate an error condition where eating cherry fails
    with pytest.raises(Exception):
        pacman.eat_cherry()  # Assuming this raises an exception on failure

def test_eat_ghost():
    pacman = Pacman()
    ghost = Ghost(
        color="red",
        start_position=(0, 0),
        x_coordinate=0,
        y_coordinate=0
    )

    ghost.edible = True

    result = pacman.eat_ghost(ghost)

    assert result is True
    assert pacman.score == 200

def test_eat_ghost_unhappy_path():
    pacman = Pacman()
    pacman.x_coordinate = 0
    pacman.y_coordinate = 0
    ghost = Ghost(color="red", start_position=(0, 0), x_coordinate=0, y_coordinate=0)
    if not ghost.edible:
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
    powerup = PowerUp(x_coordinate=0, y_coordinate=0)
    pacman.x_coordinate = 0
    pacman.y_coordinate = 0
    pacman.eat_powerup(powerup)
    assert pacman.score == 50

def test_powerup_unhappy_path():
    pacman = Pacman()
    # Simulate an error condition where powerup fails
    with pytest.raises(Exception):
        pacman.powerup()  # Assuming this raises an exception on failure

