from Dice import Dice
from dice_helper import *

def main():
    
    num_dice = int(input("How many dices do you want to roll? "))
    same_sides = input("All of the same side? (y/n) ")
    

    dices = check_inputs(same_sides, num_dice)
    
    
    ans = roll_all(dices)

    print(f"Your roll is: {ans}")
    
if __name__ == "__main__":
    main()