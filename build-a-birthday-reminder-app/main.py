#This is a simple bithday reminder app. The user can input a name and the app will return the birthday of that person if it exists in the records.

user_input = input("Which birthday are you looking for? ")

if user_input == "Chloe":
    print("Chloe's birthday is on January 2nd.")
elif user_input == "Guy":
    print("Guy's birthday is March 30th.")
elif user_input == "Baba":
    print("Baba's birthday is on January 25th.")
else:
    print("There is no record of that person's birthday.")