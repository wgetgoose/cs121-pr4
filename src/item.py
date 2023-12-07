from term import animationPrint, hold, clear, animateHold

class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.loc = None
    def describe(self):
        clear()
        animationPrint(self.desc)
        hold()
    def putInRoom(self, room):
        self.loc = room
        room.addItem(self)

class Note(Item):
    def __init__(self, name, desc):
        Item.__init__(self, name, desc)
        self.type = "note"
        self.content = ""
    def use(self, player):
        clear()
        animationPrint(self.content)
        animateHold()
    def inspect(self):
        print(self.name + " | Type: " + self.type + " | Description: " + self.desc)

class Weapon(Item):
    def __init__(self, name, desc, damage):
        Item.__init__(self, name, desc)
        self.type = "weapon"
        self.damage = damage
    def inspect(self):
        print(self.name + " | Type: Weapon, " + str(self.damage) + " damage | Description: " + self.desc)


class Potion(Item):
    def __init__(self, name, desc, heal):
        Item.__init__(self, name, desc)
        self.type = "potion"
        self.heal = heal
    def use(self, player):
        player.health = player.health + self.heal
        if player.health > 100:
            player.health = 100
        print("You now have " + str(player.health) + " health!")
        player.items.remove(self)
        hold()
    def inspect(self):
        print(self.name + " | Type: Potion, " + str(self.healing) + " healing | Description: " + self.desc)