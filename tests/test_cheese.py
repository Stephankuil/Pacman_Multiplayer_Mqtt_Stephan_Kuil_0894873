import pytest
from game.cheese import Cheese
def test_cheese_color():
    chees = Cheese(rgb_color="yellow")
    assert chees.rgb_color == "yellow"

def test_cheese_how_many_left():

    cheese1 = Cheese()
    cheese2 = Cheese()
    cheese3 = Cheese()
    cheese4 = Cheese()
    cheese5 = Cheese()

    cheese_list = [
        cheese1,
        cheese2,
        cheese3,
        cheese4,
        cheese5
    ]

    assert cheese1.how_many_left(cheese_list) == 5

def test_cheese_how_many_left_below_zero_error():
    with pytest.raises(ValueError):
        Cheese().how_many_left([])

