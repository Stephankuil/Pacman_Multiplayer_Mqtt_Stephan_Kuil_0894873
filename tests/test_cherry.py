import pytest
from game.cherry import Cherry
def test_cherry_bonus_points():
    cherry = Cherry()
    assert cherry.bonus_points == 50



