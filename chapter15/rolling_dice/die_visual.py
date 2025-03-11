from roll_die import Die
import plotly.express as px

#By default the num_sides =6 
die= Die()
die_2 = Die(10)

results =[]
for roll_num in range(50000):
    result = die.roll() + die_2.roll()
    results.append(result)
#print(results)

#Analysing the results
frequencies = []
max_result = die.num_sides + die_2.num_sides
poss_values = range(1, max_result+1)

for value in poss_values:
    frequency = results.count(value)
    frequencies.append(frequency)
#print(frequencies)

#Result visualization
title = "Results of Rolling a Six and Ten sided Die for 50_000 times"
labels = {"x":"Results", "y":"Frequency of result"}
fig = px.bar(x=poss_values, y=frequencies, title=title, labels= labels )
#fig.show()
fig.write_html("myCode/chapter15/rolling_dice/roll.html")