import os
from term import animationPrint, hold, clear, animateHold

class Item:
    def __init__(self, name, desc, id):
        self.name = name
        self.desc = desc
        self.loc = None
        self.id = id
    def describe(self):
        clear()
        animationPrint(self.desc)
        hold()
    def putInRoom(self, room):
        self.loc = room
        room.addItem(self)

class Note(Item):
    def __init__(self, name, desc, id):
        Item.__init__(self, name, desc, id)
        self.type = "note"
        self.content = ""
    def use(self, player):
        clear()
        animationPrint(self.content)
        animateHold()

class Weapon(Item):
    def __init__(self, name, desc, damage, id):
        Item.__init__(self, name, desc, id)
        self.type = "weapon"
        self.damage = damage

class Food(Item):
    def __init__(self, name, desc, heal, id):
        Item.__init__(self, name, desc, id)
        self.type = "food"
        self.heal = heal

class Potion(Item):
    def __init__(self, name, desc, heal, id):
        Item.__init__(self, name, desc, id)
        self.type = "potion"
        self.heal = heal
    def use(self, player):
        player.health = player.health + self.heal
        print("You now have " + str(player.health) + " health!")
        player.items.remove(self)
        hold()