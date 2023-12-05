from random import randint
import term

def criticalHit(hp):
    rand = randint(1, 100)
    if rand <= 10:
        return (hp * 1.25)
    else:
        return hp

def turn(attacker, receiver):
    damage = attacker.attack()
    receiver.health = round((receiver.health - damage))
    term.combatStatus(attacker, receiver, damage)

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
        term.combatSituation(player, monster, turnCount)
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
