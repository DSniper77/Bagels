import random

DIGITS = 3
GUESSES = 10

def main():
    print('''Bagels, a deductive logic game, coded by Daniel Lovegrove.
          I am thinking of a {}-digit number with no repeated digits.
          You have {} guesses to see what it is. Here are some clues:
          When I say:           That means:
            Pico                One digit is correct, but in the wrong position.
            Fermi               One digit is correct and in the correct position.
            Bagels              There are no correct digits.
          For example, if the secret number is 248 and your guess was 843,
          my response would be Fermi Pico.'''.format(DIGITS, GUESSES))
    
    while True:
        secretNum = getSecretNum()
        print("I have thought of a number.")
        print("You have {} attempts to guess the number.".format(GUESSES))

        numGuesses = 1
        while numGuesses <= GUESSES:
            guess = ""
            while len(guess) != DIGITS or not guess.isdecimal():
                print("Guess #{}".format(numGuesses))
                guess = input("> ")
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > GUESSES:
                print("You ran out of guesses!")
                print("The answer was {}.".format(secretNum))
            
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing!")

def getSecretNum():
    # returns a string made up of DIGITS unique random digits
    numbers = list("0123456789")
    random.shuffle(numbers)
    secretNum = ""
    for i in range(DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    # returns a string a clues based on the guess made against the secret number
    if guess == secretNum:
        return "You got it!"
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # a correct digit is in the correct place
            clues.append("Fermi")
        elif guess[i] in secretNum:
            # a correct digit is in the incorrect place
            clues.append("Pico")
    if len(clues) == 0:
        # there are no correct digits
        return "Bagels"
    else:
        # sort the clues to not give away their position
        clues.sort()
        # make a single string from the list of clues
        return " ".join(clues)
    
if __name__ == "__main__":
    main()