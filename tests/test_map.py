import pytest
from game.level_map import LevelMap

def test_map():
    map = LevelMap(width=10, height=10, number_of_map=1, map=LevelMap.MAP1)
    assert map.width == 10

def test_map_draw():
    level_map = LevelMap(
        map=LevelMap.MAP1,
        width=10,
        height=10,
        number_of_map=1
    )

    assert level_map.draw_map() == "Drawing map 1 with width 10 and height 10"

def test_map_width():
    map = LevelMap(width=10, height=10, number_of_map=1, map=LevelMap.MAP1)
    assert map.width == 10

def test_map_height():
    map = LevelMap(width=10, height=10, number_of_map=1, map=LevelMap.MAP1)
    assert map.height == 10

def test_numbers_of_maps():
    map = LevelMap(width=10, height=10, number_of_map=1, map=LevelMap.MAP1)
    map2 = LevelMap(width=15, height=15, number_of_map=2, map=LevelMap.MAP1)
    map3 = LevelMap(width=20, height=20, number_of_map=3, map=LevelMap.MAP1)
    assert map.number_of_map == 3

def test_is_wall():
    map = LevelMap(width=10, height=10, number_of_map=1, map=LevelMap.MAP1)
    assert map.is_wall(0, 0) == True
    assert map.is_wall(1, 1) == False

def test_is_wall_out_of_bounds():
    map = LevelMap(width=10, height=10, number_of_map=1, map=LevelMap.MAP1)
    assert map.is_wall(-1, -1) == False  # Assuming out of bounds returns False
    assert map.is_wall(10, 10) == False  # Assuming out of bounds returns False

def test_get_tile():
    map = LevelMap(width=10, height=10, number_of_map=1, map=LevelMap.MAP1)
    assert map.get_tile(0, 0) == "Wall"
    assert map.get_tile(1, 1) == "Empty"

def test_get_tile_out_of_bounds():
    map = LevelMap(width=10, height=10, number_of_map=1, map=LevelMap.MAP1)
    assert map.get_tile(-1, -1) == "Out of bounds"
    assert map.get_tile(10, 10) == "Out of bounds"

def test_find_cheese_positions():
    map = LevelMap(width=10, height=10, number_of_map=1, map=LevelMap.MAP1)
    cheese_positions = map.find_cheese_positions()
    assert cheese_positions == [(2, 2), (3, 3), (4, 4)]  # Assuming these are the cheese positions

def test_find_cheese_positions_unhappy_path():
    map = LevelMap(width=10, height=10, number_of_map=1, map=LevelMap.MAP1)
    map.cheese_positions = []  # Simulating no cheese on the map
    cheese_positions = map.find_cheese_positions()
    assert cheese_positions == []  # Should return an empty list when no cheese is found