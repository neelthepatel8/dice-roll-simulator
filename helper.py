from Dice import Dice

def check_inputs(same_sides, num_dice):
    dices = []
    if same_sides == 'y':
            sides = int(input("How many sides then? "))
            for _ in range(num_dice):
                dices.append(Dice(sides))
        
    else:
        for i in range(num_dice):
            side = int(input(f"Sides for dice {i + 1}: "))
            dices.append(Dice(side))
            
    return dices

def make_player_dict(num_players, dices):
    players = {}
    for num in range(num_players):
        name = input(f"Player {num + 1} name: ")
        players[num] = {}
        players[num]["name"] = name
        players[num]["dice"] = dices[num]
        
def play_game(dices):
    # Ask number of players
    num_players = int(input("Number of players: "))
    
    players = make_player_dict(num_players, dices)

    print("How do you want to roll:")
    print("1: Roll continously")    
    print("2: Roll After asking") 
    choice = int(input("Your choice: "))
    
    if choice == 1:
        rolls = float('inf')
    else: rolls = 1
       