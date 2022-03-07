# 1. Name:
#    Jaxon Hamm
# 2. Assignment Name:
#    Lab 01: Python Review
# 3. Assignment Description:
#    A simple guessing game where the user will define a range, and the
#    computer will pick a number for them to guess.
#
# 4. What was the hardest part? Be as specific as possible.
#    The logic of the assignement was rather easy. The difficult part was
#    learning the syntax of a new programming language. I am used to a more 
#    rigid syntax so having a looser syntax is jsuta little confusing to me.
#   
#    I also was having issues with VScode saying that there were syntax errors with things as
#    simple as print statements. After multiple reloads of the program and
#    disabling and enabling extensions it finally began to work.
#    
#    The final challenge I had was realizing that the input function was
#    returning strings rather than integers so testing the two data types was
#    causing the program to crash. I figured it out through a lot of print
#    statements.
#
# 5. How long did it take for you to complete the assignment?
#    2.5 hours

import random

# Repeat the game as long as the input is yes.
while True:
    # Game introduction
    print('This is the "guess a number" game.')
    print('You try to guess a random number in the smallest number of attempts.\n')

    # Prompt the user for how difficult the game will be. Ask for an integer.
    value_max = 0
    value_max = int(input("Pick a positive integer: "))

    # Generate a random number between 1 and the chosen value.
    value_random = random.randint(1, value_max)

    # Give the user instructions as to what he or she will be doing
    print("Guess a number between 1 and %d. " % value_max)

    # Initialize the sentinal and the array of guesses
    guesses = []
    guess = 0
    # Play the guessing game
    while True:

        # Prompt the user for a number
        guess = int(input("> "))

        # Store the number in an array so it can be displayed later
        guesses.append(guess)

        # Make a decision: was the guess too high, too low, or just right
        if guess == value_random:
            break
        elif guess > value_random:
            print("\tToo high!")
        else:
            print("\tToo low!")

    # Give the user a report: How many guesses and what the guesses where
    print("You were able to find the number in %d guesses." % len(guesses))
    print("The numbers you guesses were: " + str(guesses))

    # Determine whether to play the game again
    again = input("Play again? y/n: ").lower()

    if again == "n":
        break
