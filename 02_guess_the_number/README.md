# Number Guessing Game

## Description

This is a Python-based number guessing game. The game generates a random number between 0 and 9 and asks the user to guess the number. A hint is provided to help the user whether the number is less than 5 or 5 and greater.

## How It Works

1. The program begins by welcoming the player and explaining the game's objective, i.e., to guess a randomly generated number between 0 and 9.

2. A random number is generated using the `randrange()` function from Python's `random` module.

3. Based on the generated number, the program gives a hint to the user. If the random number is less than 5, it tells the user that the number is less than 5. If the random number is 5 or greater, it tells the user that the number is 5 or greater.

4. A line of dashes is printed to visually separate the hint from the guessing section of the game.

5. The program then enters an infinite loop where it repeatedly asks the user to guess the number.

6. If the user's guess is correct, the program congratulates the user and breaks out of the loop, ending the game.

7. If the user's guess is incorrect, the program informs the user that their guess was wrong and prompts them to try again. Another line of dashes is printed to separate the attempts visually.

## Notes

This game is a simple number guessing game intended to demonstrate basic concepts in Python such as importing modules, using conditional statements, and working with loops. It does not handle non-numeric or unexpected input. For a more robust version of this game, additional error checking and handling would be necessary.