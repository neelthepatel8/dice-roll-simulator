from Dice import Dice
from dice_helper import *
from helper import *

def start():
    
    play_game = input("Just a roll or play a full game? (Roll = r, Game = g) ")
    
    print("Define the dice type: ")
    num_dice = int(input("How many dices do you want to roll? "))
    
    if num_dice == 1:
        same_sides = 'y'
        
    else:
        same_sides = input("All of the same side? (y/n) ")
    
    if play_game == 'r':

        dices = check_inputs(same_sides, num_dice)
        
        ans = roll_all(dices)

        print(f"Your roll is: {ans}")
        
        
    
if __name__ == "__main__":
    start()