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
        eat_cheese()
        eat_powerup()
        add_score()
        eat_cherry()
    }

    class Ghosts {
        +rgb_color color
        +int start_position
        +boolean edible
        make_edible()
        make_normal()
        wall_check()
        hit_pacman()
    }
}

namespace Items {
    class Cherry {
        +int bonus_points
    }

    class Cheese {
        +rgb_color color
        how_many_left()
    }

    class Powerup {
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