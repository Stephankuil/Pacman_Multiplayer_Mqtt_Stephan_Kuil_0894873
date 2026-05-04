```mermaid
classDiagram
direction TB

class GameObject {
    +int x
    +int y
    draw()
}

class Character {
    +string name
    +int score
    move()
    wall_check()
}

class Item {
    +int points
    +boolean consumed
}

namespace Gamelogic {
    class Engine {
        +boolean running
        +int level
        +int game_status
        +int number_of_players
        if_win()
        game_over()
        game_run()
        game_resume()
        game_stop()
        draw_map()
    }

    class LevelMap {
        +list map
        +int width
        +int height
        +int number_of_map
        is_wall()
        get_tile()
        find_cheese_positions()
    }
}

namespace Characters {
    class Pacman {
        +int lives
        +blob image
        eat_cheese()
        eat_powerup()
        add_score()
        eat_cherry()
        lose_life()
        eat_ghost()
    }

    class Ghosts {
        blob image
        +rgb_color color
        +int start_position
        +boolean edible
        make_edible()
        make_normal()
        hit_pacman()
        eat_by_pacman()
    }
}

namespace Items {
    class Cherry {
        +blob image
        +int bonus_points
        respawn()
    }

    class Cheese {
        +blob image
        -rgb_color color
        how_many_left()
    }

    class Powerup {
        +blob image
        +int spawn_points
        +int amount
    }
}

GameObject <|-- Character
Character <|-- Pacman
Character <|-- Ghosts

GameObject <|-- Item
Item <|-- Cheese
Item <|-- Cherry
Item <|-- Powerup

Engine -- LevelMap
Engine -- Pacman
Engine -- Ghosts
LevelMap -- Cheese
LevelMap -- Cherry
Pacman -- Cheese
Pacman -- Cherry
Pacman -- Ghosts
Pacman -- Powerup
```