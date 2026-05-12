import pytest
from game.character import Character

class FakeLevelMap:
    def is_wall(self, x, y):

        if x < 0 or y < 0:
            return True

        return False
def test_character_name():
    character = Character(name="Test Character", score=0, x_coordinate=0, y_coordinate=0)
    assert character.name == "Test Character"
    assert character.score == 0


def test_character_move():
    fake_map = FakeLevelMap()

    character = Character(
        name="Test Character",
        score=0,
        x_coordinate=5,
        y_coordinate=5
    )

    character.move("LEFT", fake_map)

    assert character.x_coordinate == 4
    assert character.y_coordinate == 5
def test_character_move_out_of_bounds():

    fake_map = FakeLevelMap()

    character = Character(
        name="Test Character",
        score=0,
        x_coordinate=0,
        y_coordinate=0
    )

    character.move("LEFT", fake_map)

    assert character.x_coordinate == 0
    assert character.y_coordinate == 0


def test_character_score():
    character = Character(name="Test Character", score=0, x_coordinate=0, y_coordinate=0)
    character.add_score(10)
    assert character.score == 10
