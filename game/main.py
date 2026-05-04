from engine import Engine
from map import Map
from cheese import Cheese

if __name__ == "__main__":
    game_map = Map(Map.MAP, 19, 21, 1)


    engine = Engine(
        running=False,
        level=1,
        game_status="menu",
        number_of_players=1
    )

    cheese = Cheese(
        image_path="images/cheese3.png",
        positions=game_map.find_cheese_positions(),
        tile_size=40
    )

    engine.start_game(game_map, cheese)

