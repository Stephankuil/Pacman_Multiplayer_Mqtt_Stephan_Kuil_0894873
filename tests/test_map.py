from game.level_map import LevelMap


def test_map():
    level_map = LevelMap(width=10, height=10, number_of_map=1, map=LevelMap.MAP1)
    assert level_map.width == 10


def test_map_width():
    level_map = LevelMap(width=10, height=10, number_of_map=1, map=LevelMap.MAP1)
    assert level_map.width == 10


def test_map_height():
    level_map = LevelMap(width=10, height=10, number_of_map=1, map=LevelMap.MAP1)
    assert level_map.height == 10


def test_numbers_of_maps():
    map1 = LevelMap(width=10, height=10, number_of_map=1, map=LevelMap.MAP1)
    map2 = LevelMap(width=15, height=15, number_of_map=2, map=LevelMap.MAP1)
    map3 = LevelMap(width=20, height=20, number_of_map=3, map=LevelMap.MAP1)

    assert map1.number_of_map == 1
    assert map2.number_of_map == 2
    assert map3.number_of_map == 3


def test_is_wall():
    level_map = LevelMap(width=10, height=10, number_of_map=1, map=LevelMap.MAP1)

    assert level_map.is_wall(0, 0) is True
    assert level_map.is_wall(1, 1) is False


def test_get_tile():
    level_map = LevelMap(width=10, height=10, number_of_map=1, map=LevelMap.MAP1)

    assert level_map.get_tile(0, 0) == "1"
    assert level_map.get_tile(1, 1) == " "


def test_find_cheese_positions():
    level_map = LevelMap(width=10, height=10, number_of_map=1, map=LevelMap.MAP1)

    cheese_positions = level_map.find_cheese_positions()

    assert len(cheese_positions) > 0
    assert (1, 1) in cheese_positions