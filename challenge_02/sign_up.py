# from roles import janitor, programmer, secretory
from roles import *

# class SignUp:
# 
    # def __init__(self):
        # self.first_name = input("What is your first name: ")
        # self.second_name = input("What is your last name: ")
        # self.email = input("What is your email: ")
        # 
        # roles = {
            # "Janitor": janitor,
            # "Programmer": programmer,
            # "Secretory": secretory
        # }
# 
        # print("\nAvailable Positions:")
        # for role_name in roles:
            # print(f"- {role_name}")
# 
        # while True:
            # chosen_role = input("Select your position: ").strip().title()
            # if chosen_role in roles:
                # self.position = roles[chosen_role]
                # break
            # else:
                # print("Invalid choice. Please select a valid position.")
            # 


class SignUp:

    def __init__(self):
        self.get_user_details()
        self.choose_position()

    def get_user_details(self):
        self.first_name = input("What is your first name: ").title()
        self.second_name = input("What is your last name: ").title()
        self.email = input("What is your email: ")

        if self.first_name == "" or self.second_name == "" or self.email == "":
            print("Please fill in all the fields.")
            self.get_user_details()

    def choose_position(self):
        jobs = {
            "Janitor": janitor,
            "Programmer": programmer,
            "Secretory": secretory,
            "Developer": developer,
            "Manager": manager
        }

        print("\nAvailable Positions:")
        for job in jobs:
            print(f"- {job}")

        while True:
            chosen_role = input("Select your position: ").strip().title()
            if chosen_role in jobs:
                self.position = jobs[chosen_role]
                break
            else:
                print("Invalid choice. Please select a valid position.")