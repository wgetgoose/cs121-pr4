import random

class Room:
    def __init__(self, name, desc, world):
        self.name = name
        self.desc = desc
        self.exits = []
        self.world = world
        self.world.register(self)
        self.monsters = []
        self.items = []
    def addExit(self, direction, destination):
        self.exits.append([direction, destination])
    def getDestination(self, direction):
        for e in self.exits:
            if e[0] == direction:
                return e[1]
    def exitNames(self):
        s = ""
        for e in self.exits:
            s = s + "\n" + e[0] + " --> " + e[1].name
        s = s[1:]
        return s
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def addMonster(self, monster):
        self.monsters.append(monster)
    def removeMonster(self, monster):
        self.monsters.remove(monster)
    def hasItems(self):
        return self.items != []
    def getItemByName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False
    def hasMonsters(self):
        return self.monsters != []
    def getMonsterByName(self, name):
        for i in self.monsters:
            if i.name.lower() == name.lower():
                return i
        return False
    def randomNeighbor(self):
        return random.choice(self.exits)[1]
    def listItems(self):
        items = ""
        for i in self.items:
            items = items + i.name + " "
        return items