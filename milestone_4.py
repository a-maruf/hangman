# Milestone 4, Task 4
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

            # Loop through each letter in the word
            for char_index in range(len(self.word)):
                # If the letter is equal to the guess
                if self.word[char_index] == guess:
                    # Replace the corresponding "_" in the word_guessed with the guess
                    self.word_guessed[char_index] = guess
                    
                    # Reduce the variable num_letters by 1
                    self.num_letters -= 1

        else:
            # Reduce num_lives by 1
            self.num_lives -= 1

            # Print a message saying "Sorry, {letter} is not in the word."
            print(f"Sorry, {guess} is not in the word.")

            # Print another message saying "You have {num_lives} lives left."
            print(f"You have {self.num_lives} lives left.")

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