import random

# Picks a number between 1 and 100.
RAND_RANGE = random.randrange(1, 100)

# Easy -> 10 Lives
def easy():
    lives = 10
    is_end = False
    while not is_end:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess. "))
        if guess == RAND_RANGE:
            return print(f"You got it! The answer was {RAND_RANGE}")
        else:
            lives -= 1
            if guess > RAND_RANGE:
                print("Too high.\nGuess again.")
            else:
                print("Too low.\nGuess again.")
            if lives == 0:
                return print("You've run out of guesses, you lose.")

# Hard -> 5 Lives
def hard():
    lives = 5
    is_end = False
    while not is_end:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess. "))
        if guess == RAND_RANGE:
            return print(f"You got it! The answer was {RAND_RANGE}")
        else:
            lives -= 1
            if lives == 0:
                return print("You've run out of guesses, you lose.")
            if guess > RAND_RANGE:
                print("Too high.\nGuess again.")
            else:
                print("Too low.\nGuess again.")


# Starts the game
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"Pssst, the correct answer is {RAND_RANGE}")
    easy_or_hard = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if easy_or_hard == "easy":
        easy()
    else:  
        hard()

start_game()