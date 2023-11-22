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
        self.energy = 80
        self.equipped = None
        self.day = 0
    def goDirection(self, direction):
        self.loc = self.loc.getDestination(direction)
    def pickup(self, item):
        self.items.append(item)
        item.loc = self
        self.loc.removeItem(item)
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
    def die(self):
        print("You have been defeated. Try again!")
        self.alive = False