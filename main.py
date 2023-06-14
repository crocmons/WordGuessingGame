"""
File: word_guess.py
-------------------
Fill in this comment.
"""
import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Max number of guesses per game


def play_game(secret_word):
    """
    Play the game by guessing the secret word.

    Parameters:
    secret_word (str): The secret word to guess.
    """
    # Initialize the guessed word with dashes
    guessed_word = ["-"] * len(secret_word)

    # Track the number of incorrect guesses
    incorrect_guesses = 0

    # Game loop
    while True:
        print("The word now looks like this:","".join(guessed_word))
        print("You have", INITIAL_GUESSES - incorrect_guesses, "guesses left")

        # Ask the user to guess a letter
        guess = input("Type a single letter here, then press enter: ").upper()

        # Check if the guessed letter is in the secret word
        if guess in secret_word:
            print("That guess is correct.")
            # Update the guessed word with the correct positions of the guessed letter
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_word[i] = guess
        else:
            print("There are no " + guess + "'s in the word")
            incorrect_guesses += 1

        # Check if the game is over
        if "".join(guessed_word) == secret_word:
            print("Congratulations, the word is: ", secret_word)
            break

        if incorrect_guesses == INITIAL_GUESSES:
            print("Game over! You have reached the maximum number of incorrect guesses.")
            print("Sorry, you lost. The secret word was:", secret_word)
            break




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
    # index = random.randrange()
    # if index == 0:
    #     return 'JAVASCRIPT'
    # elif index == 1:
    #     return 'PYTHON'
    # elif index == 2:
    #     return 'FUNNY'
    # elif index == 3:
    #     return 'CHRIS PIECH'
    # elif index == 4:
    #     return 'MEHRAN'     
    # else:
    #     return 'COMPUTER'
    
    """
    Now working for file
    """
        
    word_list = []
    with open(LEXICON_FILE, "r") as file:
        for line in file:
            word_list.append(line.strip())

    return random.choice(word_list)    


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
