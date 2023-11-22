
# local modules
from room import Room, Origin
from player import Player
from monster import Monster
from term import clear
from world import World
import updater
import term
import item



def initialize():
    world.rooms.append(origin)
    player.location = origin
    introNote = item.Note("Welcome", "a message from those who traveled before", world.newID())
    introNote.content = "Forlorn here I write in warning, to those who travel after me.\n\
                         The cave from here is treacherous. Evils line the crevices of \n\
                         those who dare to enter. Yet, one is left no choice. Do as I have,\n\
                         kill the knaves that line the cellars, and you will find salvation.\n\
                         Whether one is the same man after this journey, alas, is your own question."
    introNote.loc = origin
    term.printIntro()

world = World()
origin = Origin("room 0")
player = Player()
initialize()
playing = True

# TO-DO: Write some code to make the text transition from intro to situation smoother
while playing and player.alive:
    term.printSituation(player)
    commandSuccess = False
    timePasses = False
    while not commandSuccess:
        commandSuccess = True
        command = input( ("\033[5m") + ">>>" + ("\033[0m") + " " )
        if not command:
            print("Invalid input, please try again")
            commandSuccess = False
            continue
        commandWords = command.split()
        if commandWords[0].lower() == "go":   #cannot handle multi-word directions
            player.goDirection(commandWords[1]) 
            timePasses = True
        elif commandWords[0].lower() == "pickup":  #can handle multi-word objects
            targetName = command[7:]
            target = player.location.getItemByName(targetName)
            if target != False:
                player.pickup(target)
            else:
                print("No such item.")
                commandSuccess = False
        elif commandWords[0].lower() == "sleep":
            world.day = world.day + 1
        elif commandWords[0].lower() == "inventory":
            player.showInventory()      
        elif commandWords[0].lower() == "help":
            showHelp()
        elif commandWords[0].lower() == ("exit" or "quit"): 
            playing = False
        elif commandWords[0].lower() == "attack":
            targetName = command[7:]
            target = player.location.getMonsterByName(targetName)
            if target != False:
                player.attackMonster(target)
            else:
                print("No such monster.")
                commandSuccess = False
        else:
            print("Invalid input, please try again")
            commandSuccess = False
    if timePasses == True:
        updater.updateAll()