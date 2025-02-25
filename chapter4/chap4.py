fruits = ["Oranges", "Bananas", "Apples", "Strawberrys", "Grapes"]

for x in fruits:
    print("Good day to eat some", x)

#test yourself 
pizzas = ["Pineapple", "Pepperoni", "cheese", "Beef", "Spicy chicken"]

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("I really like pizzas. \nPepperoni is my personal favourite!")

for values in range(1,10):
    print(values)

##Working with for loops to do some math
cube = []
for x in range(1,11):
    cubes = x**3
    cube.append(cubes)
print(cube)

power_3 = [x**3 for x in range(1,11)]
print(power_3)
print("The minimum num is", min(power_3))
print("The maximum num is", max(power_3))
###The end of using loops do some math

##Slicing
print(fruits)
print(fruits[5::-1])

my_tuples = ("Five", "5", "hello", "red")
print(my_tuples)

print(my_tuples[1:4])
print(len(my_tuples))

buffet = ("steak", "Beef stew", "Hake", "Chicken stripes", "Nuggests") 
for food in buffet:
    print(food)

#The restaurant changes its menu, replacing two of the items with different food
buffet = ("Beef burgers", "Beef stew", "Hake", "Chicken stripes", "Russian Rolls")
print("The new and revised menu:")
for food in buffet:
    print(food)