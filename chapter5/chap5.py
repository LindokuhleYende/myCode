#Try it yourself
# Alien Colors #1: Imagine an alien was just shot down in a game. Create a
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# • Write an if statement to test whether the alien’s color is green. If it is, print
# a message that the player just earned 5 points.
# • Write one version of this program that passes the if test and another that
# fails. (The version that fails will have no output.)

# Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3,
# and write an if-else chain.
# • If the alien’s color is green, print a statement that the player just earned 5
# points for shooting the alien.
# • If the alien’s color isn’t green, print a statement that the player just earned
# 10 points.
# • Write one version of this program that runs the if block and another that
# runs the else block.

# If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed
# for the appropriate color alien.

#alien_color = input("Enter alien color: choose between green, yellow and red.::")
alien_color = "red"
if alien_color == "green":
    print("Good, You just earned 5 points.")
elif alien_color == "yellow":
    print("Great, you have earned 10 points !!")
elif alien_color == "red":
    print("Congratulations!! You have earned 15 points.")
else:
    print("Sorry! There are no aliens with that color in this game. \nTry Again!!")

#Stages of life
age = 54

if age<2:
    print("Just a baby")
elif age>=2 and age<4:
    print("Just a toddler")
elif age>=4 and age<13:
    print("Just a kid")
elif age>=13 and age<20:
    print("You a now a Teen!")
elif age>=20 and age<65:
    print("You are an adult now!")
else:
    print("You are an elder")

# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user.
username = ["Siyanda", "Phindile", "Admin", "Nolitha", "Zanokuhle", "Thabisile", "Jabu", "Phonny"]

for user in username:
    if user.lower() == "admin":
        print("Hello admin,would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again!")