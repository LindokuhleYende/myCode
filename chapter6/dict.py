person1 = {"name":"Kat",
        "surname":"Moloro",
        "age":34,
        "place": "Molapo",
        "car": "Honda"
        }
print(f"The person in question is {person1['name']} {person1['surname']} is aged {person1['age']}.\nShe lives in {person1['place']} and drives the latest {person1['car']}.")
#Add a new property to person1
person1["marital status"] = "Married"
print(person1)

#Glossary
programming_words = {
    "variable": "A named container that stores a piece of data which can change throughout the program",
    "loop": "A code structure that allows you to repeat a block of instructions multiple times until a specific condition is met",
    "List": "Data structure that stores a collection of items in a specific order, allowing you to access and manipulate them as a group",
    "Dictionary": "Data structure that stores data in key-value pairs",
    "Terminal": "Text-based interface where you can type commands directly to your computer's operating system"
}
print("What is a Loop:", programming_words["loop"])
