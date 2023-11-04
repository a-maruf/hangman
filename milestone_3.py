# Milestone 3 (Task 3): Check if the guessed character is in the word
word = "apple"     # Used for test purposes

def check_guess(guess):
    # Step 2: Convert the guess into lower case
    guess = guess.lower()

    # Step 3: Check if the guess is in the word
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        # Ask the user to guess a letter
        guess = input("\nGuess a letter: ")

        # Check that the guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            # If the guess passes the checks, break out of the loop
            break
        else:
            # If the guess does not pass the checks, print a message
            print("Invalid letter. Please, enter a single alphabetical character.")

    # Step 6: Call the check_guess function to check if the guess is in the word
    check_guess(guess)

# Step 7: Call the ask_for_input function to test your code
ask_for_input()

