from world import World
from player import Player
from room import Room
from monster import Monster
from item import Weapon, Note, Potion
from term import parse

world = World()

def newID():
    global world
    return world.newID()

def newRoom(name, desc):
    global world
    # allow room to set self.world
    r = Room(name, desc, world)
    return r

def connectRooms(room1, dir1, room2, dir2):
    #creates "dir1" exit from room1 to room2 and vice versa
    room1.addExit(dir1, room2)
    room2.addExit(dir2, room1)


def generate():
    origin = newRoom("Origin", "the beginning of the end")
    player = Player()
    player.loc = origin
    pocketKnife = Weapon("Pocket Knife", "a knife you brought with you from the outside", 3)
    player.items.append(pocketKnife)
    player.equipped = pocketKnife
    introNote = Note("Jeremiah", "a message from those who traveled before")
    introNote.content = parse('content/introNote.txt')
    introNote.putInRoom(origin)
    vial = Potion("Gregory's Goo", "...ew", 20)
    tutorialMonster = Monster("Gregory", "a weakling knave", 15, 2, origin, vial)
    atreus = newRoom("Atreus", "Etched, faded inscriptions of epic figures line the walls, and you feel Athena's grace bless your heart")
    elixir = Potion("Elixir of Athena", "By her grace, you may be healed", 90)
    crypt = newRoom("King's Crypt", "Skulls line the walls. Here lies those that faltered against the King's goodwill")
    ironSword = Weapon("Iron Sword", "Yieled by King James during his reign of terror", 12)
    kingJames = Monster("Ghost of King James", "Even in death, James still reigns terror in the crypt", 22, 8, crypt, ironSword)
    msEntry = newRoom("Mineshaft Entry", "Looks janky, but the tracks seem to go somewhere...")
    msExit = newRoom("Mineshaft Exit", "Lucky that the cart works...")
    goblinCellar = newRoom("Goblin Cellar", "Home of the Great Goblins of Gilchrist")
    goblins = Monster("Goblins of Gilchrist", "A gang of 3 combative goblins", 32, 6, goblinCellar, elixir)
    finalRoom = newRoom("Jeremiah", "No escaping now")
    victory = Note("Victory", "Good job, player")
    victory.content = "Congratulations, player. In a twist of fate, you have defeated Jeremia \n"
    jeremiah = Monster("Jeremiah", "Salvation arrives", 70, 14, finalRoom, victory)
    connectRooms(origin, "left", atreus, "right")
    connectRooms(origin, "right", msEntry, "left")
    connectRooms(atreus, "up", crypt, "down")
    connectRooms(msEntry, "up", msExit, "down")
    connectRooms(msExit, "up", goblinCellar, "down")
    crypt.addExit("right", finalRoom)
    msExit.addExit("left", finalRoom)
    return [world, player]
