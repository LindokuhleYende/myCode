fruits = ["Oranges", "Bananas", "Apples", "Strawberrys", "Grapes"]

for x in fruits:
    print("Good day to eat some", x)


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
###The end of using loops do some math