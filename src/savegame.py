import os
import json
from datetime import date

savePath = os.getcwd() + "/saves"


class Save():
    def __init__(self, name):
        self.name = name
        self.date = date.today().strftime("%B %d, %Y")
        self.id = newID()
        self.dir = savePath + "/" + self.name
        os.mkdir(self.dir)
        os.mkdir(self.dir + "/player")
        os.mkdir(self.dir + "/player/items")
        os.mkdir(self.dir + "/rooms")
        d = {}
        d['name'] = self.name
        d['date'] = self.date
        d['id'] = self.id
        d['dir'] = self.dir
        with open(self.dir + "/save.json", "w") as outfile:
            json.dump(d, outfile)

def initSave(name):

    s = Save(name)
    return s

def newID():
    return 1 + len(os.listdir(savePath))

def checkSaves():
    if "saves" not in os.listdir(os.getcwd()):
        os.mkdir(os.getcwd() + "/saves")
        return False
    elif os.listdir(savePath) == []:
        return False
    else:
        return True

def playerSave(save, player):
    working = save.dir + "/player"
    dict = {}
    dict['name'] = player.name
    dict['loc'] = player.loc.name
    dict['health'] = player.health
    dict['equipped'] = player.equipped.name
    for item in player.items:
        itemSave(save, item, working)
    with open(working + "/player.json", "w") as outfile:
        json.dump(dict, outfile)

def monsterSave(save, monster, dir):
    def write(dict):
        with open(working + "/" + monster.name + ".json", "w") as outfile:
            json.dump(dict, outfile)
    working = dir + "/monsters"
    dict = {}
    dict['name'] = monster.name
    dict['desc'] = monster.desc
    dict['health'] = monster.health
    dict['damage'] = monster.damage
    dict['id'] = monster.id
    write(dict)


def itemSave(save, item, dir):
    def write(dict):
        with open(working + "/" + item.name + ".json", "w") as outfile:
            json.dump(dict, outfile)
    working = dir + "/items"
    dict = {}
    dict['name'] = item.name
    dict['desc'] = item.desc
    dict['id'] = item.id
    if item.type == "note":
        dict['type'] = item.type
        dict['content'] = item.content
        write(dict)
    elif item.type == "weapon":
        dict['type'] = item.type
        dict['damage'] = item.damage
        write(dict)
    elif item.type == "potion":
        dict['type'] = item.type
        dict['heal'] = item.heal
        write(dict)
    else:
        write(dict)

def roomSave(save, room):
    def write(dict):
        with open(working + "/room.json", "w") as outfile:
            json.dump(dict, outfile)
    working = save.dir + "/rooms/" + room.name
    os.mkdir(working)
    os.mkdir(working + "/items")
    os.mkdir(working + "/monsters")
    dict = {}
    dict['name'] = room.name
    dict['desc'] = room.desc
    dict['name'] = room.name
    exits = []
    for exit in room.exits:
        l = []
        exit = exit[:]
        l.append(exit[0])
        l.append((exit[1]).name)
        exits.append(l)
    dict['exits'] = exits

    for item in room.items:
        itemSave(save, item, working)
    for monster in room.monsters:
        monsterSave(save, monster, working)
    write(dict)