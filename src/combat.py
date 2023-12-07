from random import randint
import term


def hold():
    term.hold()

def hpCalc(attacker):
    rand = randint(1, 100)
    if rand <= 10:
        damage = round(attacker.getDamage() * 1.5, 1)
        return [damage, True]
    else:
        return [attacker.getDamage(), False]

def turn(attacker, receiver):
    damage = hpCalc(attacker)
    criticalHit = damage[1]
    damage = damage[0]
    receiver.health = receiver.health - damage
    if receiver.health <= 0:
        return receiver
    else:
        term.combatStatus(attacker, receiver, damage, criticalHit)
        hold()
        return True
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
    hold()
    while fighting == True:
        turnCount = turnCount + 1
        term.combatSituation(player, monster, turnCount)
        a = turn(first, second)
        if a != True:
            return a
        b = turn(second, first)
        if b != True:
            return b
