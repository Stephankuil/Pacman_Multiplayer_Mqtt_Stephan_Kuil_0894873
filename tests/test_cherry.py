import pytest
from game.cherry import Cherry
def test_cherry_bonus_points():
    cherry = Cherry(x_coordinate=0, y_coordinate=0)
    assert cherry.bonus_points == 50

def test_cherry_respawn_time():
    cherry = Cherry(x_coordinate=0, y_coordinate=0)
    assert cherry.respawn_time == 30

def test_cherry_respawn_time_below_zero_error():
    with pytest.raises(ValueError):
        Cherry(respawn_time=-10)


def test_cherry_respawn_coordinates():
    cherry = Cherry(x_coordinate=0, y_coordinate=0)
    cherry.respawn(new_x_coordinate=5, new_y_coordinate=5)
    assert cherry.x_coordinate == 5
    assert cherry.y_coordinate == 5

def test_cherry_respawn_negative_coordinates_error():
    cherry = Cherry(x_coordinate=0, y_coordinate=0)
    with pytest.raises(ValueError):
        cherry.respawn(new_x_coordinate=-1, new_y_coordinate=-1)
