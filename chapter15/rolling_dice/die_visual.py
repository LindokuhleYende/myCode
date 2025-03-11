from roll_die import Die
import plotly.express as px

#By default the num_sides =6 
die = Die()

results =[die.roll() for roll_num in range(100)]
#print(results)

#Analysing the results
frequencies = []
poss_values = range(1, die.num_sides+1)

for value in poss_values:
    frequency = results.count(value)
    frequencies.append(frequency)
#print(frequencies)