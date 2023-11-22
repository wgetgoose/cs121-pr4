# local modules
from room import Room, Origin
from player import Player
from monster import Monster
from term import *
from world import World
from combat import combat
from item import Weapon, Note, Food, Potion
import updater



def newID():
    global globalID
    globalID = globalID + 1
    return globalID

def initialize():
    world.rooms.append(origin)
    player.loc = origin
    introNote = Note("Jeremiah", "a message from those who traveled before", newID())
    introNote.content = """
Forlorn here I write in warning, to those who travel after me.
The cave from here is treacherous. Evils line the crevices of
those who dare to enter. Yet, one is left no choice. Do as I have,
kill the knaves that line the cellars, and you will find salvation.
Whether one is the same man after this journey, alas, is your own question.
Pursue with vigilance,
Jeremiah
"""
    introNote.putInRoom(origin)
    tutorialMonster = Monster("Gregory", "a weakling knave ", 15, 2, origin, newID())
    pocketKnife = Weapon("Pocket Knife", "a knife you brought with you from the outside", 3, newID())
    player.items.append(pocketKnife)
    tutorialPotion = Potion("Elixir", "restores health", 15, newID())
    tutorialPotion.putInRoom(origin)
    # printIntro()

globalID = -1
world = World()
origin = Origin("Origin")
player = Player()
initialize()
player.name = input("Before we begin, what is your name?\n> ")
playing = True

while playing and player.alive:
    printSituation(player)
    commandSuccess = False
    timePasses = False
    while not commandSuccess:
        commandSuccess = True
        # ASCII escape chars to make input command "blink" on certain compatible terminals
        command = input( ("\033[5m") + ">" + ("\033[0m") + " " )
        # Fixes "index out of range" when user presses enter instead of entering command
        if not command:
            print("Invalid command! Please try again")
            commandSuccess = False
            continue
        commandWords = command.split()
        firstArgument = commandWords[0].lower()
        if firstArgument == "go":   #cannot handle multi-word directions
            player.goDirection(commandWords[1]) 
            timePasses = True
        elif firstArgument == "pickup":  #can handle multi-word objects
            if len(player.items) >= 30:
                print("Inventory is full. Please drop an item.")
                commandSuccess = False
            else:
                targetName = command[7:]
                target = player.loc.getItemByName(targetName)
                if target != False:
                    player.pickup(target)
                else:
                    print("No such item")
                    commandSuccess = False
        elif firstArgument == "drop":
            targetName = command[5:]
            target = player.getItemByName(targetName)
            if target != False:
                player.drop(target)
            else:
                print("No such item")
                commandSuccess = False
        elif firstArgument == "use":
            target = command[4:]
            item = player.getItemByName(target)
            if item != False:
                item.use(player)
            else:
                print("Not a valid item. Please try again.")
                commandSuccess = False
        elif firstArgument == "equip":
            target = command[6:]
            item = player.getItemByName(target)
            if item != False:
                player.equipped = item
            else:
                print("Not a valid item. Please try again.")
                commandSuccess = False
        elif firstArgument == "sleep":
            player.day = player.day + 1
            clear()
            animationPrint("Sleep well!")
            print()
            animationPrint(". . . . . .", 0.3)
        elif firstArgument == "inventory":
            player.showInventory()
        elif firstArgument == "help":
            showHelp()
        elif firstArgument == "exit" or firstArgument == "quit" or firstArgument == "quit()":
            playing = False
        elif firstArgument == "attack":
            targetName = command[7:]
            target = player.loc.getMonsterByName(targetName)
            if target != False:
                loser = combat(player, target)
                if loser == player:
                    player.die()
                else:
                    clear()
                    print("You have defeated " + target.name + "!")
                    hold()
                    target.die()
            else:
                print("Invalid opponent. Please try again")
                commandSuccess = False
        else:
            print("Invalid command. Please try again")
            commandSuccess = False
    if timePasses == True:
        updater.updateAll()
