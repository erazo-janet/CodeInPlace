"""
File: hangman.py
-------------------
Lets play a game of hangman! 
"""

import random

LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with

def play_game(secret_word):
    """
    Add your code (remember to delete the "pass" below)
    """
    guesses = ''
    turns = 8 # how many guesses we get 
    print("The world now looks like this: ") #intro
    print("you have ",turns,"guesses left") 
    while turns > 0:
        failed = 0
        #for the first for loop, we want to display the _ first. so we will ask for 
        #user input later in the code
        for char in secret_word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1
        if failed == 0:
            print("Good Job, you guessed the word!")
            break
        print('')
        #ask for user input after the hangman _ has been displayed
        guess = input("Type a single letter here, then press enter: ").upper()
        guesses += guess
        if len(guess) == 1 and guess.isalpha(): #make sure the user is only entering 1 character
            if guess not in secret_word:
                turns -= 1
                print("There are no ",guess,"'s in the word")
                print("You have", + turns, 'more guesses')
            if turns == 0:
                print("Sorry, you lost. The secret word was", secret_word)
        else:
            print("only guess one character in the alphabet!")

def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    index = random.randrange(3)
    if index == 0:
        return 'COMPUTER'
    elif index == 1:
        return 'PYTHON'
    else:
        return 'HAPPY'



def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)

    #ask the user if they want to play again
    play_again = input("Do you want to play again? Y or N: ")
    while play_again == "Y":
        play_game(secret_word)
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()