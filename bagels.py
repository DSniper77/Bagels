"""Bagels, a game programmed by Daniel Lovegrove, initially sourced from 'The Big Book of Small Python Projects' by Al Sweigart
   A deductive logic game where you must guess a series of characters based on clues.
   Tags: short, game, puzzle"""

import random

NDIGITS = 3
NGUESSES = 10
ADIGITS = 3
AGUESSES = 20

def main():
    print("Bagels, a deductive logic game, coded by Daniel Lovegrove.")

    # game version selection between alphabetic and numeric
    print("Before we begin, would you like to play the numeric or alphabetic version?")
    version = ""
    while version != "1" and version != "2":
        version = input("1 for numeric, 2 for alphabetic: ")
    
    if version == "1":
        print('''
            I am thinking of a {}-digit number with no repeated digits.
            You have {} guesses to see what it is. Here are some clues:
            When I say:           That means:
                Pico                One digit is correct, but in the wrong position.
                Fermi               One digit is correct and in the correct position.
                Bagels              There are no correct digits.
            For example, if the secret number is 248 and your guess was 843,
            my response would be Fermi Pico.\n'''.format(NDIGITS, NGUESSES))
    elif version == "2":
        print('''
            I am thinking of a {}-character long string with no repeated characters.
            You have {} guesses to see what it is. Here are some clues:
            When I say:           That means:
                Pico                One character is correct, but in the wrong position.
                Fermi               One character is correct and in the correct position.
                Bagels              There are no correct characters.
            For example, if the secret string is fpb and your guess was bpq,
            my response would be Fermi Pico.\n'''.format(ADIGITS, AGUESSES))
    
    # main game loop:
    while True:
        # stores the secret number and confirms the quantity of numeric guesses available
        if version == "1":
            secretNum = getSecretNum()
            print("I have thought of a number.")
            print("You have {} attempts to guess the number.".format(NGUESSES))
        
        # stores the secret string and confirms the quantity of alphabetical guesses available
        elif version == "2":
            secretString = getSecretString()
            print("I have thought of a string.")
            print("You have {} attempts to guess the number.".format(AGUESSES))

        numGuesses = 1
        # start of the number guessing loop, confirming input is valid before continuing
        if version == "1":
            while numGuesses <= NGUESSES:
                guess = ""
                while len(guess) != NDIGITS or not guess.isdecimal():
                    print("Guess #{}".format(numGuesses))
                    guess = input("> ")
                
                # print out of clues based on last guess
                clues = getClues(guess, secretNum)
                print(clues)
                numGuesses += 1

                # check for ending state, both pass and fail
                if guess == secretNum:
                    break
                if numGuesses > NGUESSES:
                    print("You ran out of guesses!")
                    print("The answer was {}.".format(secretNum))
        
        # start of the string guessing loop, confirming input is valid before continuing
        elif version == "2":
            while numGuesses <= AGUESSES:
                guess = ""
                while len(guess) != ADIGITS or not guess.isalpha():
                    print("Guess #{}".format(numGuesses))
                    guess = input("> ").lower()
                
                # print out of clues based on last guess
                clues = getClues(guess, secretString)
                print(clues)
                numGuesses += 1

                # check for ending state, both pass and fail
                if guess == secretString:
                    break
                if numGuesses > AGUESSES:
                    print("You ran out of guesses!")
                    print("The answer was {}.".format(secretString))
            
    # check for another round of play, generous confirmation
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
        print("Thanks for playing!")

def getSecretNum():
    # returns a string made up of NDIGITS unique random digits
    numbers = list("0123456789")
    random.shuffle(numbers)
    secretNum = ""
    for i in range(NDIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getSecretString():
    # returns a string made up of ADIGITIS unique random alphabetical characters
    characters = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(characters)
    secretString = ""
    for i in range(ADIGITS):
        secretString += str(characters[i])
    return secretString

def getClues(guess, secret):
    # returns a string a clues based on the guess made against the secret number / string
    if guess == secret:
        return "You got it!"
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            # a correct digit / character is in the correct place
            clues.append("Fermi")
        elif guess[i] in secret:
            # a correct digit / character is in the incorrect place
            clues.append("Pico")
    if len(clues) == 0:
        # there are no correct digits / characters
        return "Bagels"
    else:
        # sort the clues to not give away their position
        clues.sort()
        # make a single string from the list of clues
        return " ".join(clues)
    
if __name__ == "__main__":
    main()