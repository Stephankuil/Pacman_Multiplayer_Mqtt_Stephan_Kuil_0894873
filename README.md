S — Single Responsibility Principle (SRP)
"Elke klasse heeft één duidelijke verantwoordelijkheid. De Pacman-klasse beheert het gedrag van Pacman, de Ghost-klasse beheert de spoken en de MQTTManager-klasse verzorgt alleen de netwerkcommunicatie via MQTT. Hierdoor heeft iedere klasse slechts één reden om gewijzigd te worden."


**Pacman class is only responsible for pacman behaviour**
https://github.com/Stephankuil/Pacman_Multiplayer_Mqtt_Stephan_Kuil_0894873/blob/0008c2675740d53c91c3e295fce5bb6580854315/game/pacman.py#L7



O — Open/Closed Principle (OCP) 

Open voor uitbreiding, gesloten voor aanpassing. 

Je moet nieuwe functionaliteit kunnen toevoegen zonder bestaande code te wijzigen. 

**from gameobject to cherry. You can create more features without changing the code. **
https://github.com/Stephankuil/Pacman_Multiplayer_Mqtt_Stephan_Kuil_0894873/blob/0008c2675740d53c91c3e295fce5bb6580854315/game/gameobject.py#L3
https://github.com/Stephankuil/Pacman_Multiplayer_Mqtt_Stephan_Kuil_0894873/blob/0008c2675740d53c91c3e295fce5bb6580854315/game/item.py#L4
https://github.com/Stephankuil/Pacman_Multiplayer_Mqtt_Stephan_Kuil_0894873/blob/0008c2675740d53c91c3e295fce5bb6580854315/game/cherry.py#L5


L — Liskov Substitution Principle (LSP) 

Een subklasse moet altijd de basisklasse kunnen vervangen. 

Als iets een Item is, moet je zonder problemen een Cherry of PowerUp kunnen gebruiken. 

https://github.com/Stephankuil/Pacman_Multiplayer_Mqtt_Stephan_Kuil_0894873/blob/0008c2675740d53c91c3e295fce5bb6580854315/game/main.py#L209



 

I — Interface Segregation Principle (ISP) 

Maak liever meerdere kleine interfaces dan één grote. 
De item classe heeft alleen item functies en geen onnodige methodes. Hiermee krijgen cherry en cheese enzo geen onnodige functies.
https://github.com/Stephankuil/Pacman_Multiplayer_Mqtt_Stephan_Kuil_0894873/blob/0008c2675740d53c91c3e295fce5bb6580854315/game/item.py#L4



 

D — Dependency Inversion Principle (DIP) 

Programmeer tegen abstracties, niet tegen concrete implementaties. 

I dont really have DIP in this project.


* Schrijf de solid principes die je hebt toegepast in je eigen woorden.
* Schrijf waarom je dingen hebt verandert naar een solid principe. Dus waarom heb ik het verbeterd en waarom werkt het goed.


**De Solid Principes in mijn pacman_mqtt project**

Hieronder staat jouw tekst iets netter geschreven, maar nog steeds in een eenvoudige stijl alsof jij hem zelf hebt geschreven.

---

# De SOLID-principes in mijn Pacman MQTT project

In mijn project heb ik 4 SOLID-principes gebruikt: **SRP, OCP, LSP en ISP**.

Ik heb deze principes toegepast om de code overzichtelijker, beter onderhoudbaar en makkelijker uitbreidbaar te maken.

In de eerste weken van dit project heb ik met behulp van AI snel een werkende versie gemaakt zonder rekening te houden met SOLID-principes. In het tweede deel van het project heb ik het project opnieuw opgebouwd waarbij ik wel rekening hield met **Test Driven Development (TDD)** en **SOLID**.

Wat je merkt als je een project maakt zonder SOLID-principes, is dat de code snel rommelig wordt. Vaak moet je dan op meerdere plekken wijzigingen maken als je één onderdeel wilt aanpassen. Dat maakt het onderhoud van de code lastig en inefficiënt.

Een voorbeeld hiervan was de `draw()` methode. Eerst had ik in de `Cheese`, `Cherry` en `PowerUp` class allemaal een eigen `draw()` methode (**OCP**). Dit was dubbele code. Daarom heb ik een algemene `Item` class gemaakt waarin de `draw()` methode staat. De subclasses kunnen deze methode gebruiken via inheritance. Hierdoor hoef ik de tekenfunctionaliteit nog maar op één plek aan te passen als ik iets wil veranderen.

Ook had ik eerst een methode in de `Ghost` class waarmee een ghost Pacman kon raken. Dit vond ik achteraf geen goede toepassing van **SRP**, omdat de `Ghost` class dan ook kennis moest hebben van de interne werking van Pacman. Daarom heb ik deze verantwoordelijkheid verplaatst naar de `Pacman` class in de methode `hit_by_ghost()`. Hierdoor heeft iedere class een duidelijkere verantwoordelijkheid.

Voor de `Item` class en de subclasses `Cherry`, `Cheese` en `PowerUp` heb ik gebruikgemaakt van **LSP**. De code hoeft namelijk niet te weten of een object een `Cherry` of een `PowerUp` is. Beide gedragen zich als een `Item`.

```python
for item in self.items:
    item.draw(self.screen, (255, 0, 255))
```

Hierdoor kan ik later eenvoudig nieuwe item-types toevoegen zonder deze code aan te passen. Als ik bijvoorbeeld een nieuw bonus-item maak dat van `Item` erft, kan deze direct in dezelfde lijst gebruikt worden.

Daarnaast heb ik gekeken naar de opbouw van de `Item` class en de subclasses. Ik heb ervoor gezorgd dat de `Item` class alleen methodes bevat die daadwerkelijk relevant zijn voor items (**ISP**). Hierdoor krijgen classes zoals `Cherry`, `Cheese` en `PowerUp` geen onnodige functies die ze toch niet gebruiken.

Dit zorgt ervoor dat de classes simpel blijven en alleen functies bevatten die logisch zijn voor die specifieke class.

Door deze SOLID-principes toe te passen is mijn code overzichtelijker geworden, makkelijker uit te breiden en eenvoudiger te onderhouden. Ook is het makkelijker om nieuwe functionaliteit toe te voegen zonder bestaande code op veel plaatsen te moeten aanpassen.







