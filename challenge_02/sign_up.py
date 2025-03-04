# from roles import janitor, programmer, secretory
from roles import *

class SignUp:

    def __init__(self):
        self.first_name = input("What is your first name: ")
        self.second_name = input("What is your last name: ")
        self.email = input("What is your email: ")
        
        roles = {
            "Janitor": janitor,
            "Programmer": programmer,
            "Secretory": secretory
        }

        print("\nAvailable Positions:")
        for role_name in roles:
            print(f"- {role_name}")

        while True:
            chosen_role = input("Select your position: ").strip().title()
            if chosen_role in roles:
                self.position = roles[chosen_role]
                break
            else:
                print("Invalid choice. Please select a valid position.")