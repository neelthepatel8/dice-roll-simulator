from Dice import Dice

def check_inputs(same_sides, num_dice):
    dices = []
    if same_sides == 'y':
            sides = int(input("How many sides then? "))
            for _ in range(num_dice):
                dices.append(Dice(sides))
        
    else:
        for i in range(num_dice):
            side = int(input(f"Sides for dice {i}: "))
            dices.append(Dice(side))
            
    return dices