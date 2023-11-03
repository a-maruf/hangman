# Milestone 3: Check if the guessed character is in the word
# Task 1: Iteratively check if the input is a valid guess

    # Step 1: While loop and set the condition to True
while True:
    # Step 2: Ask the user to guess a letter
    guess = input("\nGuess a letter: ")

    # Step 3: Check that the guess is a single alphabetical character
    if len(guess) == 1 and guess.isalpha():
        # Step 4: If the guess passes the checks, break out of the loop
        break
    else:
        # Step 5: If the guess does not pass the checks, print a message
        print("Invalid letter. Please, enter a single alphabetical character.")
