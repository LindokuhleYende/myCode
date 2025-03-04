class User:
    def __init__(self, firstname, last_name, email, location):
        self.firstname = firstname
        self.last_name = last_name
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"{self.firstname.title()} {self.last_name.title()}'s emaail address is {self.email}.")
        print(f"The user stays at {self.location}")
    def greet_user(self):
       print(f"Hello, {self.firstname.title()} {self.last_name.title()}. \nI hope you having a wonderful day")

user = User("lindo", "yende", "yndl002@myuct.ac.za", "Cape Town")
user.describe_user()
user.greet_user()