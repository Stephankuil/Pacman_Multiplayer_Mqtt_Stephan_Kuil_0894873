import pytest
import test_cherry, test_cheese, test_engine, test_main, test_pacman, test_ghosts, test_main, test_map, test_mqtt_connection, test_multi_circle, test_character, test_game_object


def test_collectionofalltests():
    test_cherry.test_cherry()
    test_cheese.test_cheese()
    test_engine.test_engine()
    test_main.test_main()
    test_pacman.test_pacman()
    test_ghosts.test_ghosts()
    test_map.test_map()
    test_main.test_main()
    test_mqtt_connection()
    test_character.test_character()
    test_multi_circle()

