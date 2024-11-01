from random import randint

# Defining a function to play the random number guessing game
def play_guessing_game():
    """
    Plays the random number guessing game.
    The computer generates a random number, and the user tries to guess it.
    
    The function provides feedback if the guess is too high or too low and counts the number of guesses.
    
    Returns:
        None
    """
    random_number = 0  # Declare local random number variable
    user_guess = 0  # Declare local userguess variable
    guess_count = 0  # Declare local guess count variable
    
    # Generate a random number between 1 and 100
    random_number = randint(1, 100)
    
    # Loop until the user guesses the correct number
    while True:
        # Prompt the user to make a guess
        user_guess = int(input("Guess the number (between 1 and 100): "))
        
        # Increment the guess count
        guess_count += 1
        
        # Check if the guess is too high, too low, or correct
        if user_guess > random_number:
            print("Too high, try again.")
        elif user_guess < random_number:
            print("Too low, try again.")
        else:
            # If the guess is correct, congratulate the user and show the number of attempts
            print(f"Congratulations! You've guessed the correct number: {random_number}")
            print(f"It took you {guess_count} guesses.")
            
            # Break out of the loop when the correct number is guessed
            break

# Defining the main function
def main():
    """
    The main function that starts the random number guessing game and allows it to be replayed.
    """
    play_again = "yes"  # Declare the local play again variable to control the game loop
    
    # Loop to keep the game running as long as the user wants to play again
    while play_again.lower() == "yes":
        play_guessing_game()  # Call the guessing game function
        
        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ")
    
    # Thank the user when they choose not to play anymore
    print("Thank you for playing!")

# Calling the main function
if __name__ == "__main__":
    main()