class Monster:
    def __init__(self, name, desc, health, damage, room, drop=None):
        self.name = name
        self.desc = desc
        self.health = health
        self.damage = damage
        self.loc = room
        self.drop = drop
        room.monsters.append(self)
    def update(self):
        return
    def moveTo(self, room):
        self.room.removeMonster(self)
        self.room = room
        room.addMonster(self)
    def deathDrop(self):
        if self.drop != None:
            self.loc.items.append(self.drop)
            self.drop.loc = self.loc
            print(self.name + " dropped a " + self.drop.name)
    def die(self):
        self.deathDrop()
        self.loc.removeMonster(self)
    def getDamage(self):
        return self.damage