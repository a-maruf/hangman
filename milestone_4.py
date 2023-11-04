# Milestone 4, Task 1
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

# Test the class with a list of words
hangman = Hangman(['apple', 'banana', 'cherry'])
print(hangman.word)
print(hangman.word_guessed)
print(hangman.num_letters)
print(hangman.num_lives)
print(hangman.word_list)
print(hangman.list_of_guesses)