#############################
#                           #
#   Week 1 Tutorial Tasks   #
#                           #
#############################

#2-1 Simple Message
message = "Hello World!"
print(message)

#2-2 Simple Messages
message = "I'm Andrew!"
print(message)

#2-3 Personal Message
first_name = "bruce"
last_name = "wayne"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()} the city needs you!"
print(message)

#2-4 Name Cases
name = "Clark Kent"
print (name.upper())
print (name.lower())
print (name.title())

#2-5 Famous Quote
print('Todd Howard once said "It just works", it did not just work')

#2-6 Famous Quote 2
famous_person = "Todd Howard"
message = "It just works"
print(f"{famous_person} once said {message}, it did not.")

#2-7 Stripping Names
my_name = '\tAndrew\n'
print(my_name.rstrip())
print(my_name.lstrip())
print(my_name.strip())

#2-8 Number Eight
print(4+4)
print(16/2)
print(2*4)
print(20-12)

#2-9 Favorite Number
fav_num = 15
message = (f"My favourite number is {fav_num}")
print(message)

#2-10 Adding Comments

#Andrew Wallace - 23-01-2022 - This is a practice program

#2-11
import this


#3-1 Names
names = ["Jason", "Bob", "James", "Brian", "Marie"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

#3-2 Greetings
message = " you are a friend"
print(names[0] + message)
print(names[1] + message)
print(names[2] + message)
print(names[3] + message)
print(names[4] + message)

#3-3 Your Own List
cars = ["BMW", "BatMobile", "Sports Car"]
message = (f"I want to own a {cars[0]}")
print(message)
message = (f"I want to own a {cars[1]}")
print(message)
message = (f"I want to own a {cars[2]}")
print(message)

#3-4 Guest List
invite_list = ["Augustus Ceasar", "Winston Churchill", "George Washington"]
print(invite_list[0] + " You are invited to dinner")
print(invite_list[1] + " You are invited to dinner")
print(invite_list[2] + " You are invited to dinner")

#3-5 Changing Guest List
print(invite_list[1] + " is unable to attend")

invite_list[1] = "King Alfred"
print(invite_list[0] + " You are invited to dinner")
print(invite_list[1] + " You are invited to dinner")
print(invite_list[2] + " You are invited to dinner")

#3-6
print("A larger table has been found and more guests will be invited!")

invite_list.insert(0, "Dwayne Johnson")
invite_list.insert(1, "Marilyn Monroe")
invite_list.append("Emma Watson")

print(invite_list[0] + " You are invited to dinner")
print(invite_list[1] + " You are invited to dinner")
print(invite_list[2] + " You are invited to dinner")
print(invite_list[3] + " You are invited to dinner")
print(invite_list[4] + " You are invited to dinner")
print(invite_list[5] + " You are invited to dinner")

#3-7 Shrinking Guest List

print(invite_list)

print(invite_list.pop(1) + " ,I'm sorry you can't come to dinner")
print(invite_list.pop(1) + " ,I'm sorry you can't come to dinner")
print(invite_list.pop(1) + " ,I'm sorry you can't come to dinner")
print(invite_list.pop(1) + " ,I'm sorry you can't come to dinner")

print(invite_list[0] + " you are still invited")
print(invite_list[1] + " you are still invited")

invite_list.remove("Dwayne Johnson")
invite_list.remove("Emma Watson")

print(invite_list)

#3-8 Seeing the World
places = ["China", "Japan", "Germany", "Cannada", "Russia", "France"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)

#3-9 Dinner Guests
print(len(invite_list))

#3-10 Every Function
languages = ["Mandarin", "Japanese", "English", "German", "Irish", "French"]
print(sorted(languages))
languages.reverse()
languages.sort()
languages.append("Russian")
languages.insert(3, "Arabic")
languages.remove("French")
print("I am learning " + languages.pop(5))
print(languages)

#3-11 Intentional error (fixed)
print("Cat")

#4-1