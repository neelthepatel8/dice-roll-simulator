from Dice import Dice

def main():
    dice = Dice(6)
    dice2 = Dice(10)
    
    
    ans = dice.roll()
    
    print(ans)
    
if __name__ == "__main__":
    main()