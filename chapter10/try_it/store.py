import json

def store_favorite_number():
    favorite_number = input("What is your favorite number? ")
    # Convert the favorite number to JSON format and save it to a file
    with open('favorite_number.json', 'w') as file:
        json.dump(favorite_number, file)
    print("Your favorite number has been stored.")

store_favorite_number()