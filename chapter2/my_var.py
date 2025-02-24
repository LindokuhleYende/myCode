first_name = "Lindokuhle"
last_name = "Yende"
day = "Moday"
print(f"Hello {first_name} {last_name}, have a lovely {day}")

my_sentence = "cats are soo scary"

print(my_sentence.title())

##title() is a string method that return the first letter of each word as an upper case

print("Today is a brand new day. \nLet's enjoy today.\nRemain forever grateful")

# \n >> new line
#.lstrip() >> removes whitespaces on the left of the string
#.rstrip() >> removes whitespaces on the right of the string

print(" Lindo".lstrip())
print("Lindo  ".rstrip())


## Removes the prefix of url
nostarch_url = "https://nostarch.com"
print(nostarch_url.removeprefix('https://'))

#There are no built in constant variables in python, but you can create an all upper
#case var just to show other programers that the variable should remain unchanged

