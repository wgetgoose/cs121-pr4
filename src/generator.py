from world import World
from player import Player
from room import Room
from monster import Monster
from item import Weapon, Note, Food, Potion
from term import parse

world = World()

def newID():
    global world
    return world.newID()

def newRoom(desc, exits=[]):
    global world
    # allow room to set self.world
    r = Room(desc, exits, world)
    return r

def connectRooms(room1, dir1, room2, dir2):
    #creates "dir1" exit from room1 to room2 and vice versa
    room1.addExit(dir1, room2)
    room2.addExit(dir2, room1)


def generate():
    origin = newRoom("Origin")
    player = Player()
    player.loc = origin
    pocketKnife = Weapon("Pocket Knife", "a knife you brought with you from the outside", 3, newID())
    player.items.append(pocketKnife)
    player.equipped = pocketKnife
    introNote = Note("Jeremiah", "a message from those who traveled before", newID())
    introNote.content = parse('content/introNote.txt')
    introNote.putInRoom(origin)
    tutorialMonster = Monster("Gregory", "a weakling knave ", 15, 2, origin, newID())
    tutorialPotion = Potion("Elixir", "restores health", 15, newID())
    tutorialPotion.putInRoom(origin)
    atreus = newRoom("Atreus")
    crypt = newRoom("King's Crypt")
    msEntry = newRoom("Mineshaft Entry")
    # redundant. pass exits during room creation?
    connectRooms(origin, "left", atreus, "right")
    connectRooms(atreus, "up", crypt, "down")
    connectRooms(origin, "right", msEntry, "left")
    return [world, player]