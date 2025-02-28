import user_info 
from user_info import create_account as ca
from user_info import my_login as log
ca(username = input("What would you like your username to be: "),
               password = input("What would you like your password to be: "), 
               firstname = input("What is your first name: "),
               lastname = input("What is your last name: "),
               location = input("Where do you stay: "))
log()