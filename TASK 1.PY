import random

# Predefined words
words = ["python", "apple", "chair", "house", "train"]

# Choose a random word
secret_word = random.choice(words)
guessed_letters = []
attempts_left = 6

print("Welcome to Hangman Game!")

while attempts_left > 0:
    # Display current word progress
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    print("Word:", display_word)

    # Check win condition
    if "_" not in display_word:
        print("You won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in secret_word:
        guessed_letters.append(guess)
        print("Good guess!")
    else:
        guessed_letters.append(guess)
        attempts_left -= 1
        print("Wrong guess! Attempts left:", attempts_left)

if attempts_left == 0:
    print("You lost! The word was:", secret_word)
