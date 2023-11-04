# Milestone 4, Task 2
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        # Convert the guessed letter to lower case
        guess = guess.lower()

        # Check if the guess is in the word
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input(self):
        while True:
            # Ask the user to guess a letter
            guess = input("\nGuess a letter: ")

            # Check that the guess is a single alphabetical character
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                # Call the check_guess function to check if the guess is in the word
                self.check_guess(guess)

                # Append the guess to the list of guesses
                self.list_of_guesses.append(guess)


# Test the class with a list of words
hangman = Hangman(['apple', 'banana', 'cherry'])
print(hangman.word)
print(hangman.word_guessed)
print(hangman.num_letters)
print(hangman.num_lives)
print(hangman.word_list)
print(hangman.list_of_guesses)
hangman.ask_for_input()