import random


# Room Class Summary
# Each room has the following lists
#   monsters --> Tracks monsters in the room, appended by functions
#       addMonster and removeMonster imported into main.py
#   exits --> tracks the connections between the rooms we create.
#       very similar to linked lists, where rooms are "nodes" and our start
#       room is the "root"
#   items --> item logic in rooms is par with monsters
#   
class Room:
    def __init__(self, desc, exits, world):
        self.desc = desc
        self.exits = exits
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
        return [e[0] for e in self.exits]
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