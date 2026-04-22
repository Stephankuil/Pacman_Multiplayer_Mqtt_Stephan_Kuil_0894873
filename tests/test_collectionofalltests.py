import pytest
import test_cherry, test_cheese, test_engine, test_main, test_pacman, test_ghosts, test_main, test_map


def test_collectionofalltests():
    test_cherry.test_cherry()
    test_cheese.test_cheese()
    test_engine.test_engine()
    test_main.test_main()
    test_pacman.test_pacman()
    test_ghosts.test_ghosts()
    test_map.test_map()
    test_main.test_main()