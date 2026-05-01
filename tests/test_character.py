import pytest
from game.character import Character


def test_character_name():
    character = Character(name="Test Character")
    assert character.name == "Test Character"

def test_character_move():
    character = Character(name="Test Character", x=0, y=0)
    character.move(dx=5, dy=3)
    assert character.x == 5
    assert character.y == 3

def test_character_move_out_of_bounds():
    character = Character(name="Test Character", x=0, y=0)
    character.move(dx=-5, dy=-3)
    assert character.x == 0  # Assuming the character cannot move out of bounds
    assert character.y == 0


def test_character_score():
    character = Character(name="Test Character")
    character.add_score(10)
    assert character.score == 10
