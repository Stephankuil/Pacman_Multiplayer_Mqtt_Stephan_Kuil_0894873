from game.powerup import PowerUp
def test_powerup_create():
    powerup = PowerUp(100, 200)
    assert powerup.x_coordinate == 100
    assert powerup.y_coordinate == 200
    assert powerup.active == False
    assert powerup.amount == 0
    assert powerup.spawn_points == 0
    assert powerup.image is None




