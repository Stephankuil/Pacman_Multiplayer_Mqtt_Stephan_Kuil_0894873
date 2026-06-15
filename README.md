# SOLID Principles Used in the Pacman Game Directory

**Commit:** f15243a
Only the files inside the `game` directory were reviewed. The examples below demonstrate where SOLID principles are applied within the project and explain why they qualify as examples of these design principles.

The **Single Responsibility Principle (SRP)** can be seen in the `MQTTManager` class. This class is responsible only for MQTT communication, including broker configuration, credentials, callbacks, publishing, and receiving messages. By keeping networking logic separate from game logic, classes such as `Pacman`, `Ghost`, and `Main` do not need to know how MQTT communication works. This gives the `MQTTManager` one clear responsibility and improves maintainability.

Another example of SRP is found in the `Ghost` class. The `move_random()` method contains all logic related to ghost movement. The `Main` class only instructs the ghosts to move and does not contain the actual movement algorithm. This separation ensures that ghost behaviour remains the responsibility of the `Ghost` class while the game loop remains the responsibility of `Main`.

The **Open/Closed Principle (OCP)** is demonstrated through the `Item` inheritance structure. The `Item` class provides shared functionality such as storing a name, points value, consumed state, and drawing behaviour. New item types can be added by creating subclasses without changing the existing `Item` implementation. This allows the system to be extended while keeping existing code stable and unchanged.

The **Liskov Substitution Principle (LSP)** is visible in classes such as `PowerUp` and `Cheese`. Both inherit from `Item` and can be used anywhere an `Item` is expected. For example, `PowerUp` extends the base item functionality while still behaving like a normal item. Likewise, `Cheese` reuses the shared drawing behaviour through `super().draw()` while adding its own specific properties. Because both classes can replace an `Item` without breaking functionality, they satisfy the Liskov Substitution Principle.

The **Interface Segregation Principle (ISP)** can be observed in the design of the `Item` class. Items only contain behaviour that is relevant to items, such as drawing and being consumed. They are not forced to implement movement, attacking, player input handling, or other unrelated functionality. This keeps classes focused on the behaviour they actually require and avoids unnecessary dependencies.

The **Dependency Inversion Principle (DIP)** is partially applied in the interaction between `Main` and `MQTTManager`. Instead of creating all required game objects internally, the `MQTTManager` receives dependencies such as `Pacman`, `Ghost` objects, and other player information through its constructor. This approach reduces coupling because the manager works with objects supplied from outside rather than constructing them itself.

A second example of DIP can be seen where the ghost collection is injected into the `MQTTManager`. By receiving the list of ghosts through the constructor, the manager becomes more flexible and easier to test. Although the implementation still depends on concrete classes rather than abstractions or interfaces, it represents a step toward dependency inversion.

Finally, SRP is also visible in the separation between the game loop and network communication. The `Main` class controls the timing of the game loop and decides when ghost positions should be updated. The actual MQTT message creation and publishing are handled by methods such as `publish_ghost_positions()` within the `MQTTManager`. This ensures that network-specific responsibilities remain isolated from gameplay logic.

Overall, the strongest SOLID examples in this project are the use of the Single Responsibility Principle through dedicated classes such as `MQTTManager`, `Ghost`, and `Main`, and the use of the Open/Closed and Liskov Substitution Principles through the inheritance structure of `Item`, `Cheese`, and `PowerUp`. Dependency Inversion is present to a limited extent through constructor injection, although it could be strengthened further by introducing abstractions or interfaces.


[SRP - MQTT Communication](https://github.com/Stephankuil/Pacman_Multiplayer_Mqtt_Stephan_Kuil_0894873/blob/f15243a2b61f6376a2ac601cdc2d306dba452598/game/mqtt_manager.py#L17-L29)

[SRP - Ghost Movement](https://github.com/Stephankuil/Pacman_Multiplayer_Mqtt_Stephan_Kuil_0894873/blob/f15243a2b61f6376a2ac601cdc2d306dba452598/game/ghosts.py#L89-L100)

[OCP - Item Base Class](https://github.com/Stephankuil/Pacman_Multiplayer_Mqtt_Stephan_Kuil_0894873/blob/f15243a2b61f6376a2ac601cdc2d306dba452598/game/item.py#L5-L31)

[LSP - PowerUp](https://github.com/Stephankuil/Pacman_Multiplayer_Mqtt_Stephan_Kuil_0894873/blob/f15243a2b61f6376a2ac601cdc2d306dba452598/game/powerup.py#L5-L19)

[LSP - Cheese](https://github.com/Stephankuil/Pacman_Multiplayer_Mqtt_Stephan_Kuil_0894873/blob/f15243a2b61f6376a2ac601cdc2d306dba452598/game/cheese.py#L5-L34)

[ISP - Item Interface](https://github.com/Stephankuil/Pacman_Multiplayer_Mqtt_Stephan_Kuil_0894873/blob/f15243a2b61f6376a2ac601cdc2d306dba452598/game/item.py#L21-L31)

[DIP - Dependency Injection in Main](https://github.com/Stephankuil/Pacman_Multiplayer_Mqtt_Stephan_Kuil_0894873/blob/f15243a2b61f6376a2ac601cdc2d306dba452598/game/main.py#L43-L52)

[DIP - Constructor Injection in MQTTManager](https://github.com/Stephankuil/Pacman_Multiplayer_Mqtt_Stephan_Kuil_0894873/blob/f15243a2b61f6376a2ac601cdc2d306dba452598/game/mqtt_manager.py#L18-L26)

[SRP - Main Controls Loop](https://github.com/Stephankuil/Pacman_Multiplayer_Mqtt_Stephan_Kuil_0894873/blob/f15243a2b61f6376a2ac601cdc2d306dba452598/game/main.py#L110-L116)

[SRP - Publish Ghost Positions](https://github.com/Stephankuil/Pacman_Multiplayer_Mqtt_Stephan_Kuil_0894873/blob/f15243a2b61f6376a2ac601cdc2d306dba452598/game/mqtt_manager.py#L147-L160)

