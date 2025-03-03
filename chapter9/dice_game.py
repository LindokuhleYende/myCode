import random
class Die:
    def __init__(self, sides = 6):
        self.sides = sides
    def roll_die(self):
        num = random.randint(1, self.sides)
        print(num)

die = Die()
print("6 sided die rolled 10 times")
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()

die_10 = Die(10)
die_20 = Die(20)
print("10 sided die rolled few times")
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()

print("20 sided die rolled few times")
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
