import os
import json
import shutil
from room import Room
from player import Player
from monster import Monster
from item import *



class Save():
    def __init__(self, name, date, id, dir):
        self.name = name
        self.date = date
        self.id = id
        self.dir = dir

def dictParse(filepath):
    dict = {}
    with open(filepath, "r") as infile:
        dict = json.loads(infile.read())
    return dict

def listSaves():
    dir = os.getcwd() + "/saves"
    for save in os.listdir(dir):
        file = dir + "/" + save + "/save.json"
        d = dictParse(file)
        print(d['name'] + ": " + d['date'])

def getSave(name):
    dir = os.getcwd() + "/saves"
    for save in os.listdir(dir):
        if save == name:
            d = dictParse(dir + "/" + name + "/save.json")
            s = Save(d['name'], d['date'], d['id'], d['dir'])
            return s
    return None

def roomLoad(save, world):
    dict = None
    for room in os.listdir(save.dir + "/rooms"):
        dir = save.dir + "/rooms/" + room
        file = dir + "/room.json"
        dict = dictParse(file)
        name = dict['name']
        desc = dict['desc']
        r = Room(name, desc, world)
        itemDir = dir + "/items"
        monsterDir = dir + "/monsters"
        itemLoad(r, itemDir)
        monsterLoad(r, monsterDir)
        r.exits = dict['exits']

def playerLoad(save, world):
    dir = save.dir + "/player"
    file = dir + "/player.json"
    dict = dictParse(file)
    p = Player()
    itemDir = dir + "/items"
    itemLoad(p, itemDir)
    p.name = dict['name']
    p.loc = world.getRoomByName(dict['loc'])
    p.health = dict['health']
    p.equipped = p.getItemByName(dict['equipped'])
    return p

def monsterLoad(room, dir):
    for monster in os.listdir(dir):
        try: 
            dict = dictParse(dir + "/" + monster)
        except IsADirectoryError:
            continue
        name = dict['name']
        desc = dict['desc']
        health = dict['health']
        damage = dict['damage']
        drop = None
        if dict['drop']:
            drop = dropLoad(dir + "/" + "items/" + dict['drop'] + ".json")
        m = Monster(name, desc, health, damage, room, drop) 

def dropLoad(dir):
    dict = dictParse(dir)
    name = dict['name']
    desc = dict['desc']
    if dict['type'] == "note":
        content = dict['content']
        i = Note(name, desc)
        i.content = content
        return i
    elif dict['type'] == "weapon":
        damage = dict['damage']
        i = Weapon(name, desc, damage)
        return i
    elif dict['type'] == "potion":
        heal = dict['heal']
        i = Potion(name, desc, heal)
        return i
    else:
        return

def itemLoad(loc, dir):
    for item in os.listdir(dir):
        dict = dictParse(dir + "/" + item)
        name = dict['name']
        desc = dict['desc']
        if dict['type'] == "note":
            content = dict['content']
            i = Note(name, desc)
            i.loc = loc
            i.content = content
            loc.items.append(i)
        elif dict['type'] == "weapon":
            damage = dict['damage']
            i = Weapon(name, desc, damage)
            i.loc = loc
            loc.items.append(i)
        elif dict['type'] == "potion":
            heal = dict['heal']
            i = Potion(name, desc, heal)
            i.loc = loc
            loc.items.append(i)
        else:
            return
        
def overwrite(dir):
    shutil.rmtree(dir)