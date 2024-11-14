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

# location functions

# main game loop
