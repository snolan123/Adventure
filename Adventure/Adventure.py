# imports
from asyncio import shield
import random
# game variables and constants
game_over = False
MAX_PLAYER_HITPOINTS = 100
player_location = ""
player_hitpoints = MAX_PLAYER_HITPOINTS
player_attack_rating = 1
player_defence_rating = 1

key_location = "rocks"
shield_location = "skeleton"
potion_location = "wizard"
sword_location = "house"

ogre_hitpoints = 20
ogre_attack_rating = 10
ogre_defence_rating = 20

house_door_unlocked = False

def item_checker():
    global player_location
    global key_location
    global shield_location
    global potion_location
    global sword_location

    if player_location == key_location:
        print("There is a key here.")
    if player_location == shield_location:
        print("There is a shield here.")
    if player_location == potion_location:
        print("There is a potion here.")
    if player_location == sword_location:
        print("There is a sword here.")

# command handlers
def attack_handler(object):
    global player_location
    global player_hitpoints
    global player_attack_rating
    global player_defence_rating
    global ogre_hitpoints
    global ogre_attack_rating
    global ogre_defence_rating
    global game_over

    if player_location == "cave" and object == "ogre":
        print("You attack the ogre.")
        damage = random.randint(-ogre_defence_rating, player_attack_rating)
        if damage > 0:
            print("You dealt", damage, "damage.")
            ogre_hitpoints -= damage
        else:
            print("You missed.")

        damage = random.randint(-player_defence_rating, ogre_attack_rating)
        if damage > 0:
            print("The ogre hit you and dealt", damage, "damage.")
            player_hitpoints -= damage
        else:
            print("The ogre missed.")

        if player_hitpoints <= 0:
            print("You died.")
            game_over = True
        elif ogre_hitpoints <= 0:
            print("You killed the ogre.")
            print("You approach the ancient treasure chest...")
            print("With bated breath, you slowly life the lid...")
            print("As the lid creaks open, a glimmer of light spills out from within..")
            print("Behold, inside the chest, a sight to behold - it's filled with gold and jewels!")
            game_over = True

def exit_handler(location):
    global player_location

    if player_location == "house" and location == "house":
        print("You exited the house.")
        house_entrance()
        item_checker()
    elif player_location == "cave" and location == "cave":
        print("You exited the cave.")
        cave_entrance()
        item_checker()
    elif player_location == "tower" and location == "tower":
        print("You exited the tower.")
        tower_entrance()
        item_checker()
    else:
        print("You are not in a", location)

def use_handler(object):
    global player_location
    global house_door_unlocked
    global key_location
    global potion_location
    global MAX_PLAYER_HITPOINTS
    global player_hitpoints

    if player_location == "house_entrance" and key_location == "player":
        print("You have unlocked the door.")
        house_door_unlocked = True
        key_location = "nothing"
    elif potion_location == "player":
        print("You have used the potion.")
        player_hitpoints += 50
        if player_hitpoints > MAX_PLAYER_HITPOINTS:
            player_hitpoints = MAX_PLAYER_HITPOINTS
        potion_location = "nothing"
    else:
        print("You do not have a", object)

def enter_handler(location):
    global player_location
    global house_door_unlocked

    if player_location == "house_entrance" and location == "house" and house_door_unlocked == True:
        house()
        item_checker()
    elif player_location == "cave_entrance" and location == "cave":
        cave()
        item_checker()
    elif player_location == "tower_entrance" and location == "tower":
        tower()
        item_checker()
    else:
        print("You can't go there.")

def drop_handler(object):
    global player_location
    global key_location
    global shield_location
    global sword_location
    global potion_location
    global player_attack_rating
    global player_defence_rating

    if key_location == "player" and object == "key":
        print("You have dropped the key.")
        key_location = player_location
    elif potion_location == "player" and object == "potion":
        print("You have dropped the potion.")
        potion_location = player_location
    elif shield_location == "player" and object == "shield":
        print("YOu have dropped the shield.")
        shield_location = player_location
        player_defence_rating -= 30
    elif sword_location == "player" and object == "sword":
        sword_location = player_location
        player_attack_rating -= 30
    else:
        print("You do not have a", object)

def pickup_handler(object):
    global player_location
    global key_location
    global shield_location
    global sword_location
    global potion_location
    global player_attack_rating
    global player_defence_rating

    if player_location == key_location and object == "key":
        print("You have picked up the key.")
        key_location = "player"
    elif player_location == potion_location and object == "potion":
        print("You have picked up the potion.")
        potion_location = "player"
    elif player_location == shield_location and object == "shield":
        print("You have picked up the shield.")
        shield_location = "player"
        player_defence_rating += 30
    elif player_location == sword_location and object == "sword":
        print("You have picked up the sword.")
        sword_location = "player"
        player_attack_rating += 30
    else:
        print("There is no", object, "here")

def move_handler(direction):
    global player_location

    if player_location == "river_1":
        if direction == "east":
            cave_entrance()
        elif direction == "south":
            river_2()
        else:
            print("You cannot move in that directon.")
    elif player_location == "cave_entrance":
        if direction == "west":
            river_1()
        elif direction == "east":
            field()
        elif direction == "south":
            meadow()
        else:
            print("You cannot move in that direction.")
    elif player_location == "field":
        if direction == "west":
            cave_entrance()
        elif direction == "south":
            house_entrance()
        else:
            print("You cannot move in that direction.")
    elif player_location == "river_2":
        if direction == "north":
            river_1()
        elif direction == "east":
            meadow()
        elif direction == "south":
            river_3()
        else:
            print("You cannot move in that direction.")
    elif player_location == "meadow":
        if direction == "north":
            cave_entrance()
        elif direction == "east":
            house_entrance()
        elif direction == "south":
            forest()
        elif direction == "west":
            river_2()
    elif player_location == "house_entrance":
        if direction == "north":
            field()
        elif direction == "south":
            tower_entrance()
        elif direction == "west":
            meadow()
        else:
            print("You cannot move in that direction.")
    elif player_location == "river_3":
        if direction == "north":
            river_2()
        elif direction == "east":
            forest()
        else:
            print("You cannot move in that direction.")
    elif player_location == "forest":
        if direction == "north":
            meadow()
        elif direction == "west":
            river_3()
        elif direction == "east":
            tower_entrance()
        else:
            print("You cannot move in that direction.")
    elif player_location == "tower_entrance":
        if direction == "north":
            house_entrance()
        elif direction == "west":
            forest()
        else:
            print("You cannot move in that direction.")

    item_checker()

def examine_handler(object):
    global player_location
    global key_location
    global shield_location

    if player_location == "river_2" and object == "rocks" and key_location == "rocks":
        print("There is a key under the rocks.")
        key_location = "river_2"

    elif player_location == "forest" and object == "skeleton" and shield_location == "skeleton":
        print("There is a shield on the skeleton.")
        shield_location = "forest"
    else:
        print("There is nothing here.")
# location functions
def river_1():
    global player_location
    player_location = "river_1"
    print("You are at the river.")

def cave_entrance():
    global player_location
    player_location = "cave_entrance"
    print("You are at the cave entrance.")

def cave():
    global player_location
    player_location = "cave"
    print("You are in a cave.")
    print("Standing before you is a towering ogre, its eyes gleaming with malice.")

def field():
    global player_location
    player_location = "field"
    print("You are in a field.")

def river_2():
    global player_location
    player_location = "river_2"
    print("You are at the river.")
    print("There are rocks here.")

def meadow():
    global player_location
    player_location = "meadow"
    print("You are in a meadow.")

def house_entrance():
    global player_location
    global house_door_unlocked
    player_location = "house_entrance"
    print("You are at a house.")

    if house_door_unlocked == True:
        print("The door is open.")
    else:
        print("The door is locked.")

def house():
    global player_location
    player_location = "house"
    print("You are in a house.")

def river_3():
    global player_location
    player_location = "river_3"
    print("You are at the river.")

def forest():
    global player_location
    player_location = "forest"
    print("You are in a forest.")
    print("There is a skeleton of an old soldier here.")

def tower_entrance():
    global player_location
    player_location = "tower_entrance"
    print("You are at a tower.")

def tower():
    global player_location
    global potion_location
    player_location = "tower"
    print("You are in a tower.")

    if potion_location == "wizard":
        print("Standing in front of you is a wizard.")
        print("Who dares enter my tower?")
        print("I have a riddle for you bold adventurer.")
        answer = input("I am tall when I am young and I am short when I am old. What am I? ").lower().strip()
        if answer == "candle":
            print("Curses!")
            print("Here is a health potion to help with your journey.")
            print("With a puff of smoke the wizard disappears.")
            potion_location = "player"
        else:
            print("Wrong!")
            print("With a wave of his hand he blasts you out the door.")
            tower_entrance()
    else:
        print("There is nothing here.")
# main game loop
meadow()

while game_over == False:
    while True:
        commands = input("What would you like to do? ").lower().strip().split()

        if len(commands) > 0:
            break

    if commands[0] == "quit":
        print("Bye bye.")
        game_over = True
    elif commands[0] == "move":
        move_handler(commands[1])
    elif commands[0] == "examine":
        examine_handler(commands[1])
    elif commands[0] == "pickup":
        pickup_handler(commands[1])
    elif commands[0] == "drop":
        drop_handler(commands[1])
    elif commands[0] == "enter":
        enter_handler(commands[1])
    elif commands[0] == "use":
        use_handler(commands[1])
    elif commands[0] == "exit":
        exit_handler(commands[1])
    elif commands[0] == "attack":
        attack_handler(commands[1])
        