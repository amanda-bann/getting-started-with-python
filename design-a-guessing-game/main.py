# import random module
import random

# Write a variable that generates a random number between 0 and 100
random_number = random.randrange(100)

correct_guess = False

while not correct_guess:
    user_input = input("Guess a number between 0 and 100: ")

    try:
        number = int(user_input) # Convert the user input to an integer
        if number == random_number:
            correct_guess = True
        elif number > random_number:
            print("Guess is too high! Try again?")
        elif number < random_number:
            print("Guess is too low! Try again?")
    except: 
        print("Enter a valid number please :) Let's try again! ")


print("You guessed the right number! Woo!!")

