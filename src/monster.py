import random
import updater
from combat import criticalHit

class Monster:
    def __init__(self, name, desc, health, damage, room, id):
        self.name = name
        self.desc = desc
        self.health = health
        self.damage = damage
        self.id = id
        self.loc = room
        room.monsters.append(self)
        # monsters are added to list of elements in global updater
        updater.register(self)
    def update(self):
        if random.random() < .5:
            self.moveTo(self.room.randomNeighbor())
    def moveTo(self, room):
        self.room.removeMonster(self)
        self.room = room
        room.addMonster(self)
    def die(self):
        self.loc.removeMonster(self)
        updater.deregister(self)
    def attack(self):
        return criticalHit(self.damage)
