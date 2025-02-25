my_class = ["Aidan", "Asanda", "Cadee", "Courtney", "Ethan", "Lesedi", "Lindo", "Marvelous", "Mieke", "Phomello","Sibu", "Ronny", "Tom", "Ulrich"]
my_class.append("Everybody")
for peer in my_class:
    print("Good Day", peer)

print(my_class[1])


my_fruit = ["Banana", "Apple", "Orange"]
my_fruit.insert(1, "Strawberry")

print(my_fruit)


top_cars = ["G-Wagon", "Omoda", "Bently", "Mersarati", "aston martin", "Rolls Royce"]
last_car = top_cars.pop()
top_cars.sort()

print(last_car)
print(top_cars)
top_cars.reverse()
print(top_cars)

places = ["Paris", "London", "Japan", "Cape Town"]
print(places)
print(sorted(places))
print(places)
print(places[4::-1])