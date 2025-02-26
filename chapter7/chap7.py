car = input("What type of car do you want to rent? ")
print(f"Let me see if I can find you a {car}.")

resturant = int(input("How many guests are in your dinner group: "))

if resturant>8:
    print("Please wait for a table!")
else:
    print("Your table is ready.. ")

num = int(input("Please enter any number: "))

if num%10 == 0:
    print(f"The number {num} is a multiple of 10")
else:
    print(f"The number {num} is not a multiple of 10")


## working while loops and user input

prompt = input("Enter start to start adding toppings to your pizza: ")
while prompt.lower() != "quit":
    toppings = input("Enter pizza toppings ")
    print(f"You will add {toppings} to your pizza")
    prompt = input("Enter quit if you want to stop adding pizza toppings ")