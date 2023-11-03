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


# Task 2: Check whether the guess is in the word

word = "apple"     # Used for test purposes

# Step 1: Create an if statement that checks if the guess is in the word
if guess in word:
    # Step 2: In the body of the if statement, print a message saying "Good guess! {guess} is in the word."
    print(f"Good guess! {guess} is in the word.")
else:
    # Step 3: Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again."
    print(f"Sorry, {guess} is not in the word. Try again.")