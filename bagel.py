"""
In Bagels, a deductive logic game, you must guess a secret three-digit number
based on clues. The game offers one of the following hints in response to your guess:
“Pico” when your guess has a correct digit in the wrong place, “Fermi” when your guess has a correct
digit in the correct place, and “Bagels” if your guess has no correct digits. You have 10 tries to guess the
secret number.
"""
import random


def main():
    NUM_DIGITS = 3
    MAX_GUESSES = 10

    print(
        """Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:
    That means:
    <Pico> - One digit is correct but in the wrong position.
    <Fermi> - One digit is correct and in the right position.
    <Bagels> - No digit is correct.
    For example, if the secret number was 248 and your guess was 843, the
    clues would be <Fermi Pico>.""".format(
            NUM_DIGITS
        )
    )
    while True:  # Main game loop
        secret_number = get_secret_number(NUM_DIGITS)
        print("I though up a number")
        print(f"You have {MAX_GUESSES} guesses.")
        num_guess = 1

        while num_guess <= MAX_GUESSES:
            guess = ""
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(
                    f"Guess #{num_guess}. Please, think about {NUM_DIGITS}-digit number:"
                )
                guess = input("> ")
            num_guess += 1

            # If user's guess is correct, stop game
            if guess == secret_number:
                print("You got it")
                break

            # Check if any digit is correct
            clue = get_clue(guess, secret_number)
            print(clue)

            if num_guess > MAX_GUESSES:
                print("You ran out of guesses.")
                print("The answer was {}.".format(secret_number))

        print("Do you want play again?(yes or nor)")
        another_game = input("> ")
        # User stops game
        if another_game.lower().startswith("n"):
            break
    print("Thanks for playing!")


def get_secret_number(num_digits):
    """Get a random secret number."""
    num = random.randint(10 ** (num_digits - 1), 10 ** num_digits)
    return str(num)


def get_clue(guess, number):
    """Return clue string with bagels, fermi, pico."""
    clue = []
    for i in range(len(guess)):
        if guess[i] == number[i]:
            clue.append("Fermi")
        elif guess[i] in number:
            clue.append("Pico")
    if len(clue) == 0:
        return "Bagels"
    else:
        # Sort the clues into alphabetical to not give information away
        clue.sort()
        return " ".join(clue)


if __name__ == "__main__":
    main()
