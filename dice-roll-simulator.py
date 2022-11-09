from Dice import Dice
from dice_helper import *
from helper import *

def start():
    
    game_type = input("Just a roll or play a full game? (Roll = r, Game = g) ")
    
    print("Define the dice type: ")
    num_dice = int(input("How many dices do you want to roll? "))
    
    if num_dice == 1:
        same_sides = 'y'
        
    else:
        same_sides = input("All of the same side? (y/n) ")
    
    dices = check_inputs(same_sides, num_dice)
    
    if game_type == 'r':
        ans = roll_all(dices)
        print(f"Your roll is: {ans}")
    
    else:
        end_game = 'n'
        while end_game != 'y':
            play_game(dices)
            end_game = input("End Game? (y/n) ")
        
    
if __name__ == "__main__":
    start()