import os
import random
import term
from combat import criticalHit

class Player:
    def __init__(self):
        self.name = "Player"
        self.loc = None
        self.items = []
        self.health = 70
        self.alive = True
        self.equipped = None
        self.day = 0
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
    def attack(self):
        if self.equipped == None:
            return
        else:
            damage = self.equipped.damage
            return criticalHit(damage)
    def getItemByName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return False
    def die(self):
        term.playerDeath(self)