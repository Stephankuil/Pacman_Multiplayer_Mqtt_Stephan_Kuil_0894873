import pytest
from inspiration.cherry import Cherry
def test_cherry_bonus_points():
    cherry = Cherry()
    assert cherry.bonus_points == 50

def test_cherry_respawn_time():
    cherry = Cherry()
    assert cherry.respawn_time == 30

def test_cherry_respawn_time_below_zero_error():
    with pytest.raises(ValueError):
        Cherry(respawn_time=-10)



