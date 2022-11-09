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
        players[num]["dice"] = dices
    return players
        
def play_round(players, choice):
    for player in players:
        name = players[player]["name"]
        current_dices = players[player]["dice"]
        ans = 0
        for dice in current_dices:
            ans += dice.roll()
            print(f"{name}'s roll: {ans}")
        if choice == 2:
            input("Press any key for next roll: ")
            
def play_game(dices):
    # Ask number of players
    num_players = int(input("Number of players: "))
    
    players = make_player_dict(num_players, dices)

    print("How do you want to roll each player:")
    print("1: Roll continously")    
    print("2: Roll After asking for next player") 
    choice = int(input("Your choice: "))
    
    end = 'y'
    while end != 'n':
        play_round(players, choice)
        print("Round Complete! ")
        end = input("Play next round? (y/n) ")
        
    return 

    
        
    
    
       