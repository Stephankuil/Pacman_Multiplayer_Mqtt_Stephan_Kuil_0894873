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

In mijn project heb ik 4 solid principes gebruikt. Dat zijn SRP, OCP, LSP en ISP. 
Dit doe ik om de goede overzichtelijker, beter onderhoudbaar en makkelijk uitbreidbaar te maken.
Ik heb in dit project in de eerste 4 weken met behulp van AI snel een project gemaakt zonder rekening te houden met SOLID principes. En daarna in het tweede deel van het project nogmaals het project gemaakt en wel rekening gehouden met Test Driven Development en SOLID. 
Wat je ziet als je het project maakt zonder SOLID principes heb je eigenlijk geen clean code. Dat betekent dat je ongeveer alles in je code moet aanpassen als je 1 verandering doet. Dit is erg inefficient. Dus eerst zou ik in de cheese, powerup, cherry class ook draw methode hebben(**OSP**). Dit is dubbele code dus heb ik een item class gemaakt waar de draw methode instaat die gebruikt kan worden door cheese, cherry en powerup. Zo zorg je ervoor dat je als de draw methode moet worden aangepast je dat slechts 1x in item hoeft te doen. Ook had ik in de ghost class dat ghosts pacman opeten. Maar dit is niet SRP omdat je dan ook de pacman class nodig hebt. Dus heb ik die methode verplaatst naar pacman class. Dat is de hit_by_ghost methode.(**SRP**). Ook voor de items en de subclasse cherry, cheese en powerup. hiermee hoeft De code hier niet te weten of het item een Cherry of een PowerUp is. Beide gedragen zich als een Item.(**LSP**). Als ik later nog een subclasse bedenk kan die ook gewoon met die code gebruikt worden.

for item in self.items:
    item.draw(self.screen, (255, 0, 255))


Ook heb ik bij het kijken naar de item class en de cherry, cheese en powerup. gezorgt dat item class geen methodes heeft die door sommige subclasses niet gebruikt worden. Hierdoor blijven de classes simpel. Dus nu hebben classes alleen functies die logisch of nodig zijn voor die class. (**ISP**)






