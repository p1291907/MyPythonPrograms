# a function that generates a random number
# for generating a random float number use random.uniform()
# use random module
import random
def random_float():
    test = random.uniform(1,1000)
    print(test)
# this function asks the user to guess the number that the random module generated,
# and it compares the user's guess to the actual number, the program keeps asking for user's input until the user guesses the number correctly
def random_integer():
    guess = int(input("Guess the number that I'm thinking about between 1 and 1000: "))
    tries = 1
    
    while guess != random_number:
# how far guess is from the number 
        close_guess = guess - random_number
        if 0 < close_guess <= 10:
            print("Getting warm but still high, try again: ")
            guess = int(input("Guess again: "))
        elif guess > random_number and guess <= 1000:
            print("Your guess is too high, try again: ")
            guess = int(input("Guess again: "))
        elif 0 > close_guess >= -10:
            print("Getting warm but still low, try again: ")
            guess = int(input("Guess again: "))
        elif guess < random_number and guess > 0:
            print("Your guess is too low, try again: ")
            guess = int(input("Guess again: "))
        else:
            print("Number has to be between 1 and 1000")
            guess = int(input("Guess again: "))
        tries += 1
        
    print("Congrats, you won, it took you", tries, "guesses")
# The main function uses the random module to generate a random number between 1 and 1000    
# Ask the user if they want to play a game? once they say yes, the game starts
# The random_integer() function is called. Once the game starts
# the user gets the prompt if they want to play again, the game restarts and keeps going until the user enters n

again = 'Y'
answer = input("Would you like to play a game? Enter y or n: ")
answer = answer.upper()
random_number = random.randint(1,1000)
if answer == 'Y':
    print("Let's play")
    random_integer()
    again = input("Enter Y if you want to play the game again ")
    again = again.upper()
    while again == 'Y':
        random_number = random.randint(1,1000)
        random_integer()
        again = input("Enter Y if you want to play the game again ")
    print("Good game, come again!")
else:
    print("Goodbye")


