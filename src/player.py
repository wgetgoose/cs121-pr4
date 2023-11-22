import os
import random
from term import clear
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
        clear()
        print("You are currently carrying:")
        print()
        for i in self.items:
            print(i.name)
        print()
        input("Press enter to continue...")
    def attack(self):
        if self.equipped == None:
            return
        else:
            damage = self.equipped.damage
            return criticalHit(damage)
    def getItemByName(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return False

    def die(self):
        print("You have been defeated. Try again!")
        self.alive = False