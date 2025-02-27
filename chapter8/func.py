def display_message():
    print("We are learning about functions in chapter8")
display_message()

def favorite_book(title):
    print("The name of my favorite books is", title)
favorite_book("It ends with us")

def describe_city(city, country= "RSA"):
    print(f"{city} is in {country}")
    if city=="Pretoria":
        return f"{city}, ooh so you use a Gautrain.."
    elif city == "Jhb":
        return f"{city}, have you seen Vilakazi street"
    elif city == "Cpt":
        return f"{city}, have you been to Camps bay"
    elif city == "Kimberly":
        return f"{city}, have you seen the big hole of Diamonds"
    else:
        return f"I don't know {city}"
    
output = describe_city(input("Enter your city: "))
print(output)

#8-7. Album:
def make_album(artist_name, album_title):
    album = {
        'artist': artist_name,
        'title': album_title
    }
    return album
while True:
    print("\nEnter the album details. (Enter 'q' at any time to quit)")

    artist = input("Artist name: ")
    if artist == 'q':
        break

    title = input("Album title: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print("\nAlbum created:", album)

# Creating three dictionaries for different albums
# album1 = make_album('Taylor Swift', '1989')
# album2 = make_album('Ed Sheeran', 'Divide')
# album3 = make_album('Adele', '25')

# Printing the albums
# print(album1)
# print(album2)
# print(album3)

#8.9Messages: 
# Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints each text message.

messages = ["Good day","Sleep well", "Did you have breakfast today?"]
def show_messages(message):
    messages.append(message)
    return messages
print(show_messages("Hello"))

# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
# Write a function called send_messages() that prints each text message
# and moves each message to a new list called sent_messages as it’s printed. 
# After calling the function, print both of your lists to make sure 
# the messages were moved correctly.

def send_messages():
    sent_messages = []
    i = 0
    while i<len(messages):
        sent_messages.append(messages[i])
        #messages.remove(messages[i])
    return sent_messages
print(messages)
print(send_messages())
    
    