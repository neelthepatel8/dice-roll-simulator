from Dice import Dice
from dice_helper import *

def main():
    dice = Dice(6)
    dice2 = Dice(10)
    
    
    ans = roll_all([dice, dice2])
    
    print(ans)
    
if __name__ == "__main__":
    main()