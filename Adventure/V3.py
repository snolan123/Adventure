# imports
import random
# game variables and constants
game_over = False
MAX_PLAYER_HITPOINTS = 100
player_location = ""
player_hitpoints = MAX_PLAYER_HITPOINTS
player_attack_rating = 1
player_defence_rating = 1
player_name = ""

bread_location = "bench"
shield_location = "skeleton"
potion_location = "wizard"
sword_location = "tree"

ogre_hitpoints = 20
ogre_attack_rating = 10
ogre_defence_rating = 20

def item_checker():
    global player_location
    global bread_location
    global shield_location
    global potion_location
    global sword_location

    if player_location == bread_location:
        print("There is a loaf of bread here.")
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

def exit_handler():
    global player_location

    if player_location == "house":
        print("You exited the house.")
        house_entrance()
        item_checker()
    elif player_location == "cave":
        print("You exited the cave.")
        cave_entrance()
        item_checker()
    elif player_location == "tower":
        print("You exited the tower.")
        tower_entrance()
        item_checker()
    else:
        print("You are not inside anything")

def use_handler(object):
    global player_location
    global house_door_unlocked
    global potion_location
    global MAX_PLAYER_HITPOINTS
    global player_hitpoints

    if object == "bread" and bread_location == "player":
        print("You have unlocked the door.")
        player_hitpoints += 5
        if player_hitpoints > MAX_PLAYER_HITPOINTS:
            player_hitpoints = MAX_PLAYER_HITPOINTS
        bread_location = "nothing"
    elif object == "potion" and potion_location == "player":
        print("You have used the potion.")
        player_hitpoints += 50
        if player_hitpoints > MAX_PLAYER_HITPOINTS:
            player_hitpoints = MAX_PLAYER_HITPOINTS
        potion_location = "nothing"
    else:
        print("You do not have a", object)

def enter_handler():
    global player_location
    global house_door_unlocked

    if player_location == "house entrance":
        house()
        item_checker()
    elif player_location == "cave entrance":
        cave()
        item_checker()
    elif player_location == "tower entrance":
        tower()
        item_checker()
    else:
        print("You can't go there.")

def drop_handler(object):
    global player_location
    global bread_location
    global shield_location
    global sword_location
    global potion_location
    global player_attack_rating
    global player_defence_rating

    if bread_location == "player" and object == "bread":
        print("You have dropped the bread.")
        bread_location = player_location
    elif potion_location == "player" and object == "potion":
        print("You have dropped the potion.")
        potion_location = player_location
    elif shield_location == "player" and object == "shield":
        print("You have dropped the shield.")
        shield_location = player_location
        player_defence_rating -= 30
    elif sword_location == "player" and object == "sword":
        sword_location = player_location
        player_attack_rating -= 30
    else:
        print("You do not have a", object)

def pickup_handler(object):
    global player_location
    global bread_location
    global shield_location
    global sword_location
    global potion_location
    global player_attack_rating
    global player_defence_rating

    if (player_location == bread_location or bread_location == "bench") and object == "bread":
        print("You have picked up the bread.")
        bread_location = "player"
    elif player_location == potion_location and object == "potion":
        print("You have picked up the potion.")
        potion_location = "player"
    elif player_location == shield_location and object == "shield":
        print("You have picked up the shield.")
        shield_location = "player"
        player_defence_rating += 30
    elif (player_location == sword_location or sword_location == "tree") and object == "sword":
        print("You have picked up the sword.")
        sword_location = "player"
        player_attack_rating += 30
    else:
        print("There is no", object, "here")

def move_handler(direction):
    global player_location

    if player_location == "cave entrance":
        if direction == "south":
            forest()
        else:
            print("You cannot move in that direction.")
    elif player_location == "meadow":
        if direction == "west":
            forest()
        else:
            print("You cannot move in that direction.")
    elif player_location == "house entrance":
        if direction == "south":
            tower_entrance()
        elif direction == "west":
            meadow()
        else:
            print("You cannot move in that direction.")
    elif player_location == "forest":
        if direction == "north":
            meadow()
        elif direction == "east":
            tower_entrance()
        elif direction == "west":
            meadow()
        else:
            print("You cannot move in that direction.")
    elif player_location == "tower entrance":
        if direction == "north":
            house_entrance()
        elif direction == "west":
            forest()
        else:
            print("You cannot move in that direction.")

    item_checker()

def examine_handler(object):
    global player_location
    global shield_location

    if player_location == "forest" and object == "skeleton" and shield_location == "skeleton":
        print("You pull back the cape to reveal a sword and shield still in good condition.")
        shield_location = "forest"
        sword_location = "forest"
    else:
        print("There is nothing here.")

# location functions
def cave_entrance():
    global player_location
    player_location = "cave entrance"
    print("The dark cave entrance looms ominously, with a cool, damp air and faint echoes beckoning you inside.")

def cave():
    global player_location
    player_location = "cave"
    print("Inside the cave, the air is cool and damp, with jagged rocks lining the walls and a faint, eerie glow emanating from deep within the shadows.")
    print("Standing before you is a towering ogre, its eyes gleaming with malice.")

def meadow():
    global player_location
    player_location = "meadow"
    print("The meadow is a peaceful haven, with soft grass underfoot, vibrant \
wildflowers blooming in every color, and the air filled with the sweet scent of nature and the hum of bees.")

def house_entrance():
    global player_location
    global house_door_unlocked
    player_location = "house entrance"
    print("A quaint cottage with weathered stone walls and a wooden door slightly ajar, surrounded by an overgrown garden and a stone path.")

def house():
    global player_location
    global bread_location
    player_location = "house"
    print("The inside of the house is cozy, with a warm fire crackling in the hearth, \
    wooden furniture scattered around, and the smell of fresh-baked bread lingering in the air.")
    if bread_location == "bench":
        print("There is a warm loaf of bread sitting on the bench.")

def forest():
    global player_location
    global sword_location
    player_location = "forest"
    print("The dense forest is filled with towering trees, soft moss underfoot, and the rich scent of pine, with only the rustling of leaves breaking the silence.")
    print("There is a skeleton of an old soldier here.")

def tower_entrance():
    global player_location
    player_location = "tower entrance"
    print("The towering stone archway of the ancient tower stands before you, its oak door reinforced with iron and a sense of mystery in the air.")

def tower():
    global player_location
    global potion_location
    player_location = "tower"
    print("The wizard's tower is an ancient, towering structure filled with shelves of arcane tomes, glowing potions, and strange artifacts.")

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
while player_name == "":
    player_name = input("What is your name brave adventurer? ")

print("Welcome brave", player_name)

meadow()

while game_over == False:
    while True:
        commands = input("What would you like to do brave " + player_name + "? ").lower().strip().split()

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
        enter_handler()
    elif commands[0] == "use":
        use_handler(commands[1])
    elif commands[0] == "exit":
        exit_handler()
    elif commands[0] == "attack":
        attack_handler(commands[1])
        