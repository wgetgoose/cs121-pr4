# local modules
from room import Room
from player import Player
from monster import Monster
from world import World
from generator import generate
from combat import combat
from item import Weapon, Note, Potion
import term
import savegame
import load

def initialize():
    global player
    global world
    g = generate()
    world = g[0]
    player = g[1]
    player.name = input("Before we begin, what is your name?\n" + inputChar)
    # term.printIntro()

def createSave(name):
    global player
    global world
    s = savegame.initSave(name)
    for room in world.rooms:
        savegame.roomSave(s, room)
    savegame.playerSave(s, player)
    return s

def loadSave(save):
    global player
    global world
    global currSave
    load.roomLoad(save, world)
    for room in world.rooms:
        for entry in room.exits:
            entry[1] = world.getRoomByName(entry[1])
    player = load.playerLoad(save, world)
    currSave = save

def overwriteSave(save):
    global currSave
    savename = save.name
    load.overwrite(save.dir)
    currSave = createSave(savename)


inputChar = term.inputChar()
world = World()
player = None
currSave = None

if savegame.checkSaves() == False:
    initialize()
else:
    command = input("Would you like to load a save? Y/N: ")
    if command == "Y":
        load.listSaves()
        target = input("Please select save file by name: ")
        s = load.getSave(target)
        loadSave(s)
    if command == "N":
        initialize()

playing = True

while playing and player.alive:
    term.printSituation(player)
    commandSuccess = False
    timePasses = False
    while not commandSuccess:
        commandSuccess = True
        command = input(inputChar)
        # Fixes "index out of range" when user presses enter instead of entering command
        if not command:
            print("Invalid command! Please try again")
            commandSuccess = False
            continue

        commandWords = command.split()
        firstArgument = commandWords[0].lower()

        if firstArgument == "go":
            player.goDirection(commandWords[1]) 
            timePasses = True
        elif firstArgument == "pickup":
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
        elif firstArgument == "inventory":
            player.showInventory()
        elif firstArgument == "help":
            term.showHelp()
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
                    term.clear()
                    print("You have defeated " + target.name + "!")
                    term.hold()
                    target.die()
            else:
                print("Invalid opponent. Please try again")
                commandSuccess = False
        elif firstArgument == "save":
            target = command[5:]
            if target == "list":
                load.listSaves()
            if target == "":
                print("Creating new save...")
                createSave(input("Name of save?: "))
            else:
                save = load.getSave(target)
                if save != None:
                    overwriteSave(save)
                else:
                    print("Error, try again")
                    commandSuccess = False
        else:
            print("Invalid command. Please try again")
            commandSuccess = False
