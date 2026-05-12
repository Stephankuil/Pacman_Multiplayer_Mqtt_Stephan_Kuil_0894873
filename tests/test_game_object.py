import pytest

from game.gameobject import GameObject
def test_gameobject_initialization():
    gameobject = GameObject(x_coordinate=5, y_coordinate=10, image="test_image.png")
    assert gameobject.x_coordinate == 5
    assert gameobject.y_coordinate == 10
    assert gameobject.image == "test_image.png"


def test_gameobject_has_draw_method():
    gameobject = GameObject(x_coordinate=0, y_coordinate=0, image=None)
    assert hasattr(gameobject, "draw")
    assert callable(getattr(gameobject, "draw"))


def test_gameobject_draw_runs_without_error():
    gameobject = GameObject(x_coordinate=0, y_coordinate=0, image=None)
    try:
        gameobject.draw(screen=None)  # Assuming draw can handle a None screen for testing
    except Exception as e:
        pytest.fail(f"draw method raised an exception: {e}")

def test_gameObject_draw():
    class FakeScreen:
        def blit(self, image, coordinates):
            pass

    fake_screen = FakeScreen()
    gameobject = GameObject(x_coordinate=0, y_coordinate=0, image="test_image.png")
    try:
        gameobject.draw(screen=fake_screen)
    except Exception as e:
        pytest.fail(f"draw method raised an exception: {e}")

def test_gameobject_draw_unhappy_path():
    pass