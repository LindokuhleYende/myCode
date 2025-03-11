from roll_die import Die

#By default the num_sides =6 
die = Die()

results =[die.roll() for roll_num in range(10)]
print(results)