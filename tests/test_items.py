import pytest
from game.item import Item
def test_item_initialization():
    item = Item(name="Power Pellet", points=100)
    assert item.name == "Power Pellet"
def test_item_points():
    item = Item(name="Power Pellet", points=100)
    assert item.points == 100

def test_consumed_items():
    item = Item(name="Power Pellet", points=100)
    assert not item.consumed
    item.consume()
    assert item.consumed

