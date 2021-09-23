"""
Week 1, Challenge 3

Create a guessing game where the user has to guess a number between 1
and 100.

Tools:
- basic operators and variables
- if/elif/else statements
- while loops
"""

# Import libraries
import random

# Set constants
N = 100

# Initializing variables
answer = random.randint(1, N+1)
correct = False
num_guesses = 0

while not correct:
    # Get the guess
    guess = int(input(f'Enter a guess between 1 and {N}: '))
    num_guesses += 1

    # Correct answer
    if guess == answer:
        correct = True

    # Too high
    elif guess > answer:
        print('Too high!')

    else:
        print('Too low!')

print(f'Correct! The answer was {answer}. You took {num_guesses} guesses.')
