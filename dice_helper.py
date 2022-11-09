from Dice import Dice

def roll_all(dices):
    sum = 0
    for dice in dices:
        sum += dice.roll()
    
    return sum