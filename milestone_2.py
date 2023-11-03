import random   # Part of Task 2

# Task 1
favorite_fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
word_list = favorite_fruits
print(word_list)

# Task 2
word = random.choice(word_list)
print(word)

# Task 3
guess = input("\nEnter a single letter: ")

# Task 4
if len(guess) == 1 and guess.isalpha():
    print("\nGood guess!")
else:
    print("\nOpps! This is not a valid input.")