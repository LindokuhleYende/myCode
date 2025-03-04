import json

def read_favorite_number():
    try:
        # Read the favorite number from the file and print a message
        with open('favorite_number.json', 'r') as file:
            favorite_number = json.load(file)
        print(f"I know your favorite number! It's {favorite_number}.")
    except FileNotFoundError:
        print("No favorite number found. Please run the first program to store your favorite number.")

read_favorite_number()