from random import randint
from term import combatSituation, hold

def criticalHit(hp):
    rand = randint(1, 100)
    if rand <= 10:
        return round((hp * 1.25), 1)
    else:
        return hp

def turn(attacker, receiver):
    damage = attacker.attack()
    receiver.health = round((receiver.health - damage), 1)
    print(attacker.name + " deals " + str(damage) + " damage to " + receiver.name + ". Their health is now " + str(receiver.health))

def combat(player, monster):
    first = randint(0,1)
    fighting = True
    turnCount = 0
    if first == 0:
        first = player
        second = monster
    else:
        first = monster
        second = player
    print(first.name + " goes first")
    while fighting == True:
        turnCount = turnCount + 1
        combatSituation(player, monster, turnCount)
        hold()
        turn(first, second)
        if second.health <= 0:
            hold()
            return second
        hold()
        turn(second, first)
        if first.health <= 0:
            hold()
            return first
        hold()
