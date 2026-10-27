
import random

WORDS = ["python", "apple", "tiger", "school", "computer"]
MAX_ATTEMPTS = 6


def display_status(word, guessed_letters, attempts_left):
    """Display the current game status."""
    hidden_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )

    print(f"\nWord: {hidden_word}")
    print(f"Incorrect attempts remaining: {attempts_left}")
    print(
        "Guessed letters: "
        + (", ".join(sorted(guessed_letters)) if guessed_letters else "None")
    )


def play_game():
    """Run one round of Hangman."""
    word = random.choice(WORDS)
    guessed_letters = set()
    incorrect_guesses = set()

    print("\n" + "=" * 35)
    print("          HANGMAN GAME")
    print("=" * 35)
    print("Guess the hidden word, one letter at a time.")

    while len(incorrect_guesses) < MAX_ATTEMPTS:
        display_status(
            word,
            guessed_letters,
            MAX_ATTEMPTS - len(incorrect_guesses)
        )

        guess = input("\nEnter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter a single letter.")
            continue

        if guess in guessed_letters or guess in incorrect_guesses:
            print("You already guessed that letter. Try another.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("Correct guess!")
        else:
            incorrect_guesses.add(guess)
            print("Incorrect guess!")

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed: {word}")
            print("Result: YOU WIN!")
            return

    print(f"\nOut of attempts! The correct word was: {word}")
    print("Result: GAME OVER")


def main():
    while True:
        play_game()

        choice = input("\nWould you like to play again? (y/n): ")
        if choice.strip().lower() != "y":
            print("\nThank you for playing Hangman!")
            break
if __name__ == "__main__":
    main()
