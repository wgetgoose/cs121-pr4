import os
from time import sleep

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# dynamic text print speed
def animationPrint(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        sleep(delay)
    return ""

def hold():
    return input(("Press enter to continue: "))

def animateHold():
    return input(animationPrint("Press enter to continue: "))

def printSituation(player):
    clear()
    print("It is Day " + str(player.day))
    print("You are currently located in " + str(player.loc.desc))
    print()
    if player.loc.hasMonsters():
        print("Mobs:")
        for m in player.loc.monsters:
            print(m.name)
        print()
    if player.loc.hasItems():
        print("This room contains the following items:")
        for i in player.loc.items:
            print(i.name)
        print()
    print("You can go in the following directions:")
    for e in player.loc.exitNames():
        print(e)
    print()

def combatSituation(player, monster, turn):
    clear()
    print("Turn " + str(turn) + " | Your health: " + str(player.health) + " | " + monster.name + "'s health: " + str(monster.health))

def showHelp():
    clear()
    print("go <direction> -- moves you in the given direction")
    print("inventory -- opens your inventory")
    print("sleep -- replenish tiredness and the world begins a new day")
    print("pickup <item> -- picks up the item")
    print("attack <monster> -- attacks the given enemy")
    print()
    input("Press enter to continue...")


# Don't like how messy the text is. Will probably change these to text files or some other sort of storage.
def printIntro():
    clear()
    intro = """You find yourself lying face first in the dirt, groggy and flustered, unsure of where you are.
Rolling over, you see the sun shining down through a hole in the ground.
Of course, this is where you just fell through...
Out of the corner of your eye you see a sheet of paper. To pick it up, use the commands available by typing \"help\"
"""
    animationPrint(intro)
    sleep(0.1)
    animateHold()