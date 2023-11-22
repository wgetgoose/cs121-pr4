import os
from time import sleep

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# dynamic text print speed
def animationPrint(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        sleep(delay)

def printIntro():
    clear()
    # intro = "You find yourself lying face first in the dirt, groggy and flustered, unsure of where you are.\n"
    # intro2 = "Rolling over, you see the sun shining down through a hole in the ground.\nOf course, this is where you just fell through.\n"
    # intro3 = "Out of the corner of your eye you see a sheet of paper. To pick it up, use the commands available by typing \"help\".\n" 
    # animationPrint(intro)
    # sleep(0.1)
    # animationPrint(intro2)
    # sleep(0.1)
    # animationPrint(intro3)
    return input("Press enter to continue: ")


def printSituation(player):
    print(player.location.desc)
    print()
    if player.location.hasMonsters():
        print("This room contains the following monsters:")
        for m in player.location.monsters:
            print(m.name)
        print()
    if player.location.hasItems():
        print("This room contains the following items:")
        for i in player.location.items:
            print(i.name)
        print()
    print("You can go in the following directions:")
    for e in player.location.exitNames():
        print(e)
    print()

def showHelp():
    clear()
    print("go <direction> -- moves you in the given direction")
    print("inventory -- opens your inventory")
    print("nearby -- shows items nearby in the room")
    print("sleep -- allows the player to replenish tiredness")
    print("pickup <item> -- picks up the item")
    print()
    input("Press enter to continue...")