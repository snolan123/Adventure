# imports
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
        