# local modules
from room import Room
from player import Player
from monster import Monster
from world import World
from generator import generate
from combat import combat
from item import Weapon, Note, Food, Potion
import updater
import term

def initialize():
    global player
    global world
    g = generate()
    world = g[0]
    player = g[1]

inputChar = term.inputChar()
world = None
player = None
initialize()
player.name = input("Before we begin, what is your name?\n" + inputChar)
printIntro()
playing = True

while playing and player.alive:
    printSituation(player)
    commandSuccess = False
    timePasses = False
    while not commandSuccess:
        commandSuccess = True
        # ASCII escape chars to make input command "blink" on certain compatible terminals
        command = input(inputChar)
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
            if player.equipped == None:
                print("Please equip a weapon")
                commandSuccess = False
                continue
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
