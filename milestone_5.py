# Milestone 5, Task 1
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game.

        Parameters:
        word_list (list): A list of words for the game.
        num_lives (int): The number of lives the player has at the start of the game. Defaults to 5.
        """
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Check if the guessed letter is in the word.

        Parameters:
        guess (str): The letter guessed by the player.
        """
        # Convert the guessed letter to lower case
        guess = guess.lower()
        print(f"'check_guess error check: game.num_letters > 0': num_lives: {self.num_lives}, num_letters: {self.num_letters}")
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
        """
        Ask the user to guess a letter and check if the guess is in the word.
        """
        while True:
            # Check if the game is over before asking for another guess
            if self.num_lives <= 0 or self.num_letters == 0:
                break

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


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives <= 0:
            print("You lost!")
            break
        elif game.num_letters == 0:
            print("Congratulations. You won the game!")
            break
        else:
            print(f"'play_game' function 'elif game.num_letters > 0': num_lives: {game.num_lives}, num_letters: {game.num_letters}")
            game.ask_for_input()


# Test the game with a list of words
play_game(['apple', 'banana', 'cherry'])


# if __name__ == "__main__":
#     # Test the class with a list of words
#     hangman = Hangman(['apple', 'banana', 'cherry'])
#     # print(hangman.word)
#     # print(hangman.word_guessed)
#     # print(hangman.num_letters)
#     # print(hangman.num_lives)
#     # print(hangman.word_list)
#     # print(hangman.list_of_guesses)
#     hangman.ask_for_input()