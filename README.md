# Random Number Guessing Game

## Description
This Python program allows the user to play a random number guessing game. The computer generates a random number between 1 and 100, and the user tries to guess it. After each guess, the program provides feedback on whether the guess is too high or too low. When the user correctly guesses the number, the program congratulates them and displays the total number of guesses.

## Features
- **Random Number Generation**: The computer generates a random number within a specified range (1 to 100).
- **Guess Feedback**: Provides feedback to the user on whether their guess is too high or too low.
- **Replay Option**: After completing a game, the user is asked if they want to play again.

## Usage

1. Clone or download the script.
2. Run the script from the terminal or command line:

   ```bash
   python guessing_game.py
   ```

3. Follow the prompts to guess the number.

### Example
```plaintext
Guess the number (between 1 and 100): 50
Too low, try again.
Guess the number (between 1 and 100): 75
Too high, try again.
Guess the number (between 1 and 100): 63
Congratulations! You've guessed the correct number: 63
It took you 3 guesses.
```

## Functions

- **`play_guessing_game()`**: Runs the game, allowing the user to guess a randomly generated number and providing feedback.
    - **Returns**: None

- **`main()`**: Manages the game loop, allowing the user to play multiple times and control the flow of the program.

## Requirements
- **Python 3.x**

## License
This project is licensed under the MIT License.