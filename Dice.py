from random import randint

class Dice():
    def __init__(self, sides):
        self.sides = sides
    
    def get_sides(self):
        return self.sides
    
    def set_sides(self, sides):
        self.sides = sides
        
    # Dice Methods:
    def roll(self):
        return randint(1, self.sides)        
    