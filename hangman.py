import random
import pyautogui
import os

os.makedirs("screenshots", exist_ok=True)

# Save the current screen
pyautogui.screenshot("screenshots/game_start.png")

# List of words
words = [
    "python",
    "computer",
    "developer",
    "keyboard",
    "programming",
    "internship",
    "software",
    "algorithm",
    "database",
    "network"
]

# Select a random word
secret_word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("=" * 40)
print("      WELCOME TO HANGMAN GAME")
print("=" * 40)


while incorrect_guesses < max_attempts:

    display_word = ""

    # Display guessed letters
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord :", display_word)

    # Check win
    if "_" not in display_word:
        print("\n🎉 Congratulations!")
        print("You guessed the word:", secret_word)
        break

    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct Guess!")
    else:
        incorrect_guesses += 1
        remaining = max_attempts - incorrect_guesses
        print("❌ Wrong Guess!")
        print("Remaining Attempts:", remaining)

if incorrect_guesses == max_attempts:
    print("\nGame Over!")
    print("The correct word was:", secret_word)

print("\nThank you for playing!")