import term

class Player:
    def __init__(self):
        self.name = "Player"
        self.loc = None
        self.items = []
        self.health = 70
        self.alive = True
        self.equipped = None
    def goDirection(self, direction):
        self.loc = self.loc.getDestination(direction)
    def pickup(self, item):
        self.items.append(item)
        item.loc = self
        self.loc.removeItem(item)
    def drop(self, item):
        self.loc.addItem(item)
        item.loc = self.loc
        self.items.remove(item)
    def showInventory(self):
        term.showInventory(self)
    def getItemByName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return False
    def die(self):
        term.playerDeath(self)
    def getDamage(self):
        return self.equipped.damage