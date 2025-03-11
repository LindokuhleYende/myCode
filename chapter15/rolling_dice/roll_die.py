from random import randint

class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
    def roll(self):
        #return a random integer between 1 and 6(by default)
        #num_sides = 6 unless user changes it by inputing argument
        return randint(1, self.num_sides)