import random

class Player:
    def __init__(self, name, hitpoints, attack_rating, defence_rating):
        self.name = name
        self.items = []
        self.location = 0
        self.attack_rating = attack_rating
        self.defence_rating = defence_rating
        self.hitpoints = hitpoints

    def move(self, direction):
        if direction in self.location.exits and self.location.exits[direction].canMove() == True:
            self.location = self.location.exits[direction]
            print(f"You move {direction} to a {self.location.name}.")
            self.location.describe()
            self.location.moveTo(self)
        else:
            print("You can't go that way.")

    def pickup(self, item_name):
        for item in self.location.items:
            if item.name == item_name:
                item.pickup(player)
                self.items.append(item)
                self.location.items.remove(item)
                print(f"You picked up a {item.name}.")
                return
        
        print(f"There is no {item_name} here")

    def drop(self, item_name):
        for item in self.items:
            if item.name == item_name:
                item.drop(player)
                self.location.items.append(item)
                self.items.remove(item)
                print(f"You dropped a {item.name}.")
                return
        
        print(f"You do not have a {item_name}")

    def use(self, item_name):
        for item in self.items:
            if item.name == item_name:
                item.use(self)
                self.location.useItem(item, self)
                return
        
        print(f"You do not have a {item_name}")

    def attack(self):
        if self.location.monster != 0:
            print(f"You attack the {self.location.monster.name}.")
            damage = random.randint(-self.location.monster.defence_rating, self.attack_rating)
            if damage > 0:
                print("You dealt", damage, "damage.")
                self.location.monster.hitpoints -= damage
            else:
                print("You missed.")

            damage = random.randint(-self.defence_rating, self.location.monster.attack_rating)
            if damage > 0:
                print(f"The {self.location.monster.name} hit you and dealt", damage, "damage.")
                self.hitpoints -= damage
            else:
                print(f"The {self.location.monster.name} missed.")

            if self.location.monster.hitpoints <= 0:
                print(f"You killed the {self.location.monster.name}.")
                self.location.monster = 0
        else:
            print("There is no monster here")

class Item:
    def __init__(self, name):
        self.name = name

    def pickup(self, player):
        pass

    def drop(self, player):
        pass

    def use(self, player):
        pass

class Sword(Item):
    def __init__(self):
        Item.__init__(self, "sword")

    def pickup(self, player):
        player.attack_rating += 30

    def drop(self, player):
        player.attack_rating -= 30

class Potion(Item):
    def __init__(self):
        Item.__init__(self, "potion")

    def use(self, player):
        player.hitpoints += 30

class Shield(Item):
    def __init__(self):
        Item.__init__(self, "shield")

    def pickup(self, player):
        player.defence_rating += 30

    def drop(self, player):
        player.defence_rating -= 30

class Monster:
    def __init__(self, name, description, hitpoints, attack_rating, defence_rating):
        self.name = name
        self.description = description
        self.hitpoints = hitpoints
        self.attack_rating = attack_rating
        self.defence_rating = defence_rating

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.exits = {}
        self.monster = 0

    def describe(self):
        print(self.description)
        for item in self.items:
            print(f"There is a {item.name} here")

        if self.monster != 0:
            print(f"There is a {self.monster.name} here")
            print(self.monster.description)

    def useItem(self, item, player):
        pass

    def canMove(self):
        return True

    def moveTo(self, player):
        pass

    def examine(self, item):
        pass

class RiverWithRocks(Location):
    def __init__(self, name, description):
        Location.__init__(self, name, description)
        self.examined_rocks = False

    def describe(self):
        Location.describe(self)
        print("There are rocks here")

    def examine(self, item):
        if item == "rocks":
            if self.examined_rocks == False:
                print("There is a key here")
                self.items.append(Item("key"))
                self.examined_rocks = True
            else:
                print("There is nothing here")
        else:
            print(f"There is no {item} here")
     
class House(Location):
    def __init__(self, name, description):
        Location.__init__(self, name, description)
        self.unlocked = False

    def canMove(self):
        return self.unlocked == True

class HouseEntrance(Location):
    def __init__(self, name, description):
        Location.__init__(self, name, description)

    def useItem(self, item, player):
        if item.name == "key":
            self.exits["inside"].unlocked = True
            player.items.remove(item)
            print("You unlocked the door.")
        else:
            print("Nothing happens.")

class Forest(Location):
    def __init__(self, name, description):
        Location.__init__(self, name, description)
        self.examined_skeleton = False

    def describe(self):
        Location.describe(self)
        print("There is a skeleton of an old soldier here")

    def examine(self, item):
        if item == "skeleton":
            if self.examined_skeleton == False:
                print("There is a shield here")
                self.items.append(Shield())
                self.examined_skeleton = True
            else:
                print("There is nothing here")
        else:
            print(f"There is no {item} here")

class Tower(Location):
    def __init__(self, name, description):
        Location.__init__(self, name, description)
        self.has_wizard = True

    def describe(self):
        Location.describe(self)

        if self.has_wizard == True:
            print("Before you stands a wise wizard in deep purple robes, their staff crackling with mystical energy as they gaze at you with an air of both mystery and power.")

    def moveTo(self, player):
        if self.has_wizard == True:
            print("I have a riddle for you bold adventurer.")
            answer = input("I am tall when I am young and I am short when I am old. What am I? ").lower().strip()
            if answer == "candle":
                print("Curses!")
                print("Here is a health potion to help with your journey.")
                print("With a puff of smoke the wizard disappears.")
                player.items.append(Potion())
                self.has_wizard = False
            else:
                print("Wrong!")
                print("With a wave of his hand he blasts you out the door.")
                player.location = self.location.exits["outside"]
                player.location.describe()
                player.location.moveTo()

river_1 = Location("river", "The crystal-clear river flows gently, its waters sparkling in the sunlight, with tall grasses swaying along the banks.")
cave = Location("cave", "Inside the cave, the air is cool and damp, with jagged rocks lining the walls and a faint, eerie glow emanating from deep within the shadows.")
cave_entrance = Location("cave entrance", "The dark cave entrance looms ominously, with a cool, damp air and faint echoes beckoning you inside.")
field = Location("field", "A vast, open field stretches before you, dotted with colorful wildflowers and swaying grasses beneath a bright sky.")
river_with_rocks = RiverWithRocks("river", "The crystal-clear river flows gently, its waters sparkling in the sunlight, with tall grasses swaying along the banks.")
meadow = Location("meadow", "The meadow is a peaceful haven, with soft grass underfoot, vibrant wildflowers blooming in every color, and the air filled with the sweet scent of nature and the hum of bees.")
house = House("house", "The inside of the house is cozy, with a warm fire crackling in the hearth, wooden furniture scattered around, and the smell of fresh-baked bread lingering in the air.")
house_entrance = HouseEntrance("house entrance", "A quaint cottage with weathered stone walls and a wooden door slightly ajar, surrounded by an overgrown garden and a stone path.")
river_3 = Location("river", "The crystal-clear river flows gently, its waters sparkling in the sunlight, with tall grasses swaying along the banks.")
forest = Forest("forest", "The dense forest is filled with towering trees, soft moss underfoot, and the rich scent of pine, with only the rustling of leaves breaking the silence.")
tower = Tower("tower", "The wizard's tower is an ancient, towering structure filled with shelves of arcane tomes, glowing potions, and strange artifacts.")
tower_entrance = Location("tower entrance", "The towering stone archway of the ancient tower stands before you, its oak door reinforced with iron and a sense of mystery in the air.")

river_1.exits["east"] = cave_entrance
river_1.exits["south"] = river_with_rocks
cave_entrance.exits["east"] = field
cave_entrance.exits["west"] = river_1
cave_entrance.exits["inside"] = cave
cave.exits["outside"] = cave_entrance
field.exits["west"] = cave_entrance
field.exits["south"] = house_entrance
river_with_rocks.exits["north"] = river_1
river_with_rocks.exits["east"] = meadow
river_with_rocks.exits["south"] = river_3
meadow.exits["north"] = cave_entrance
meadow.exits["east"] = house_entrance
meadow.exits["south"] = forest
meadow.exits["west"] = river_with_rocks
house_entrance.exits["north"] = field
house_entrance.exits["south"] = tower_entrance
house_entrance.exits["west"] = meadow
house_entrance.exits["inside"] = house
house.exits["outside"] = house_entrance
river_3.exits["north"] = river_with_rocks
river_3.exits["east"] = forest
forest.exits["north"] = meadow
forest.exits["east"] = tower_entrance
forest.exits["west"] = river_3
tower_entrance.exits["west"] = forest
tower_entrance.exits["north"] = tower_entrance
tower_entrance.exits["inside"] = tower
tower.exits["outside"] = tower_entrance

ogre = Monster("ogre", "The ogre stands towering before you, its hulking figure covered in rough, mossy skin, with wild, unkempt hair and glowing eyes that burn with a fierce, menacing glare.", 100, 10, 20)
cave.monster = ogre

house.items.append(Sword())

name = ""

while name == "":
    name = input("What is your name brave warrior? ")

print(f"Welcome brave {name}")

player = Player(name, 100, 1, 1)
player.location = meadow
player.location.describe()

game_over = False
while game_over == False:
    commands = input("What do you want to do? ").strip().lower().split()
    if commands[0] == "quit":
        print("Thanks for playing!")
        game_over = True
    elif commands[0] == "move":
        player.move(commands[1])
    elif commands[0] == "examine":
        player.location.examine(commands[1])
    elif commands[0] == "pickup":
        player.pickup(commands[1])
    elif commands[0] == "drop":
        player.drop(commands[1])
    elif commands[0] == "use":
        player.use(commands[1])
    elif commands[0] == "attack":
        player.attack()

    if player.hitpoints <= 0:
        print("You died.")
        game_over = True
    elif ogre.hitpoints <= 0:
        print("You approach the ancient treasure chest...")
        print("With bated breath, you slowly life the lid...")
        print("As the lid creaks open, a glimmer of light spills out from within..")
        print("Behold, inside the chest, a sight to behold - it's filled with gold and jewels!")
        game_over = True