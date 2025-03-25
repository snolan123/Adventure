class Player:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.location = 0

    def move(self, direction):
        if direction in self.location.exits and self.location.exits[direction].canMove() == True:
            self.location = self.location.exits[direction]
            print(f"You move {direction} to a {self.location.name}.")
            self.location.describe()
        else:
            print("You can't go that way.")

    def pickup(self, item_name):
        for item in self.location.items:
            if item.name == item_name:
                self.items.append(item)
                self.location.items.remove(item)
                print(f"You picked up a {item.name}.")
                return
        
        print(f"There is no {item_name} here")

    def drop(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.location.items.append(item)
                self.items.remove(item)
                print(f"You dropped a {item.name}.")
                return
        
        print(f"You do not have a {item_name}")

class Item:
    def __init__(self, name):
        self.name = name

    def pickup(self, player):
        pass

    def drop(self, player):
        pass

    def use(self, player):
        pass

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

    def moveTo(self):
        pass

    def useItem(self, item):
        pass

    def canMove(self):
        return True

    def exmaine(self, item):
        pass

class RiverWithRocks(Location):
    def __init__(self, name, description):
        Location.__init__(self, name, description)
        self.examined_rocks = False

    def describe(self):
        Location.describe(self)
        print("There are rocks here")

    def exmaine(self, item):
        if item == "rocks":
            if self.examined_rocks == False:
                print("There is a key here")
                self.items.append(Item("key"))
                self.examined_rocks = True
            else:
                print("There is nothing here")
        else:
            print(f"There is no {item} here")
            

river_1 = Location("river", "The crystal-clear river flows gently, its waters sparkling in the sunlight, with tall grasses swaying along the banks.")
cave = Location("cave", "Inside the cave, the air is cool and damp, with jagged rocks lining the walls and a faint, eerie glow emanating from deep within the shadows.")
cave_entrance = Location("cave entrance", "The dark cave entrance looms ominously, with a cool, damp air and faint echoes beckoning you inside.")
field = Location("field", "A vast, open field stretches before you, dotted with colorful wildflowers and swaying grasses beneath a bright sky.")
river_with_rocks = RiverWithRocks("river", "The crystal-clear river flows gently, its waters sparkling in the sunlight, with tall grasses swaying along the banks.")
meadow = Location("meadow", "The meadow is a peaceful haven, with soft grass underfoot, vibrant wildflowers blooming in every color, and the air filled with the sweet scent of nature and the hum of bees.")
house = Location("house", "The inside of the house is cozy, with a warm fire crackling in the hearth, wooden furniture scattered around, and the smell of fresh-baked bread lingering in the air.")
house_entrance = Location("house entrance", "A quaint cottage with weathered stone walls and a wooden door slightly ajar, surrounded by an overgrown garden and a stone path.")
river_3 = Location("river", "The crystal-clear river flows gently, its waters sparkling in the sunlight, with tall grasses swaying along the banks.")
forest = Location("forest", "The dense forest is filled with towering trees, soft moss underfoot, and the rich scent of pine, with only the rustling of leaves breaking the silence.")
tower = Location("tower", "The wizard's tower is filled with ancient books, strange glowing potions on shelves, and a mystical aura that seems to hum with arcane energy.")
tower_entrance = Location("tower entrance", "The towering stone archway of the ancient tower stands before you, its oak door reinforced with iron and a sense of mystery in the air.")
tower_entrance.building = tower

river_1.exits = {"east": cave_entrance, "south": river_with_rocks}
cave_entrance.exits = {"east": field, "south": meadow, "west": river_1, "inside": cave }
cave.exits = {"outside": cave_entrance }
field.exits = {"east": cave_entrance, "south": house_entrance }
river_with_rocks.exits = {"north": river_1, "east": meadow, "south": river_3}
meadow.exits = {"north": cave_entrance, "east": house_entrance, "south": forest, "west":river_with_rocks}
house_entrance.exits = {"north": field, "south": tower_entrance, "west": meadow, "inside": house}
house.exits = {"outside": house_entrance}
river_3.exits = {"north": river_with_rocks, "east": forest}
forest.exits = {"north": meadow, "east": tower_entrance, "west":river_3}
tower_entrance.exits = {"west": forest, "north": house_entrance, "inside": tower}
tower.exits = {"outside": tower_entrance}


ogre = Monster("ogre", "The ogre stands towering before you, its hulking figure covered in rough, mossy skin, with wild, unkempt hair and glowing eyes that burn with a fierce, menacing glare.", 100, 10, 20)
cave.monster = ogre

name = ""

while name == "":
    name = input("What is your name brave warrior? ")

print(f"Welcome brave {name}")

player = Player(name)
player.location = meadow
player.location.describe()

while True:
    commands = input("What do you want to do? ").strip().lower().split()
    if commands[0] == "quit":
        print("Thanks for playing!")
        break
    elif commands[0] == "move":
        player.move(commands[1])
    elif commands[0] == "examine":
        player.location.exmaine(commands[1])
    elif commands[0] == "pickup":
        player.pickup(commands[1])