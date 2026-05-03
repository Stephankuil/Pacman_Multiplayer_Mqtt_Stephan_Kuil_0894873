import pytest
from game.map import Map
def test_map():
    map = Map(widdth=10, height=10, number_of_map=1)
    assert map.width == 10

def test_map_draw():
    map = Map(widdth=10, height=10, number_of_map=1)
    assert map.draw() == "Drawing map 1 with width 10 and height 10"

def test_map_width():
    map = Map(widdth=10, height=10, number_of_map=1)
    assert map.width == 10

def test_map_height():
    map = Map(widdth=10, height=10, number_of_map=1)
    assert map.height == 10

def test_numbers_of_maps():
    map = Map(widdth=10, height=10, number_of_map=1)
    map2 = Map(widdth=15, height=15, number_of_map=2)
    map3 = Map(widdth=20, height=20, number_of_map=3)
    assert map.number_of_map == 3

def test_is_wall():
    map = Map(widdth=10, height=10, number_of_map=1)
    assert map.is_wall(0, 0) == True
    assert map.is_wall(1, 1) == False

def test_is_wall_out_of_bounds():
    map = Map(widdth=10, height=10, number_of_map=1)
    assert map.is_wall(-1, -1) == False  # Assuming out of bounds returns False
    assert map.is_wall(10, 10) == False  # Assuming out of bounds returns False

def test_get_tile():
    map = Map(widdth=10, height=10, number_of_map=1)
    assert map.get_tile(0, 0) == "Wall"
    assert map.get_tile(1, 1) == "Empty"

def test_get_tile_out_of_bounds():
    map = Map(widdth=10, height=10, number_of_map=1)
    assert map.get_tile(-1, -1) == "Out of bounds"
    assert map.get_tile(10, 10) == "Out of bounds"

def test_find_cheese_positions():
    map = Map(widdth=10, height=10, number_of_map=1)
    cheese_positions = map.find_cheese_positions()
    assert cheese_positions == [(2, 2), (3, 3), (4, 4)]  # Assuming these are the cheese positions

def test_find_cheese_positions_unhappy_path():
    map = Map(widdth=10, height=10, number_of_map=1)
    map.cheese_positions = []  # Simulating no cheese on the map
    cheese_positions = map.find_cheese_positions()
    assert cheese_positions == []  # Should return an empty list when no cheese is found