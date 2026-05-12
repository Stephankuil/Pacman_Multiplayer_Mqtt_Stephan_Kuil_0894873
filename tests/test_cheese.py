import pytest
from inspiration.cheese import Cheese
def test_cheese_color():
    chees = Cheese(color="yellow")
    assert chees.color == "yellow"

def test_cheese_how_many_left():
    chees = Cheese(color="yellow", quantity=5)
    assert chees.how_many_left() == 5

def test_cheese_how_many_left_below_zero_error():
    with pytest.raises(ValueError):
        Cheese(color="yellow", quantity=-1)


