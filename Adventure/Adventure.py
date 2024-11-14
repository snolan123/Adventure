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
        