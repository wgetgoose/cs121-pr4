import os
from time import sleep

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def inputChar():
    return ("\033[5m") + ">" + ("\033[0m") + " "

def parse(filepath):
    with open(filepath, "r") as file:
        data = file.read()
    return data

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
    print("Health: " + str(player.health) + " | Location: " + str(player.loc.desc) + " | Equipped: " + str((player.equipped.name)))
    print()
    if player.loc.hasMonsters():
        print(str(player.loc.desc) + "'s Occupants:")
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
    animationPrint("Turn " + str(turn) + " | Your health: " + str(player.health) + " | " + monster.name + "'s health: " + str(monster.health) + "\n", 0.01)
    hold()

def combatStatus(attacker, receiver, damage, criticalHit):
    data = (attacker.name + " deals " + str(damage) + " damage to " + receiver.name + ". Their health is now " + str(receiver.health))
    if criticalHit == True:
        print("Critical Hit! " + data)
    else:
        print(data)


def showHelp():
    clear()
    print(parse("content/help.txt"))
    input("Press enter to continue...")


# Don't like how messy the text is. Will probably change these to text files or some other sort of storage.
def printIntro():
    clear()
    intro = parse('content/welcome.txt')
    animationPrint(intro)
    sleep(0.1)
    animateHold()

def showInventory(player):
    clear()
    print("You are currently carrying:")
    print()
    for i in player.items:
        print(i.name)
    print()
    input("Press enter to continue...")

def playerDeath(player):
    print("You have been defeated. Try again!")
    player.alive = False