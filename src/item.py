import os

def clear():
    # clear shell commands dependent in windows or not windows
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, name, desc, id):
        self.name = name
        self.desc = desc
        self.loc = None
        self.id = id
    def describe(self):
        clear()
        print(self.desc)
        print()
        input("Press enter to continue...")
    def putInRoom(self, room):
        self.loc = room
        room.addItem(self)

class Note(Item):
    def __init__(self, name, desc, id):
        Item.__init__(self, name, desc, id)
        self.type = "note"
        self.content = ""

class Weapon(Item):
    def __init__(self, name, desc, id, damage):
        Item.__init__(self, name, desc, id)
        self.type = "weapon"
        self.damage = damage

class Food(Item):
    def __init__(self, name, desc, id, heal):
        Item.__init__(self, name, desc, id)
        self.type = "food"
        self.heal = heal