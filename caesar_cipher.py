"""
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It
encrypts letters by shifting them over by a certain number of places in the alphabet
"""


def main():
    """"""
    # Get step(direction and value)
    step_direction = ""
    while step_direction not in ("e", "d"):  # keep looping until th user enters e or d
        print("Do you want to (e)ncrypt or (d)ecrypt?")
        step_direction = input(">").strip().lower()

    if step_direction == "e":
        step = 1
    else:
        step = -1

    step_value = ""
    # keep looping until user enters correct value(0-25)
    while not (step_value.isdecimal() and 0 <= int(step_value) <= 25):
        print("Please enter the key (0 to 25) to use.")
        step_value = input(">")
    step = step * int(step_value)

    # Get message
    word = "encrypt" if step_direction == "e" else "decrypt"
    print(f"Enter the message to {word}.")
    message = input(">")
    new_message = get_chipher(message, step)
    print(new_message)


def get_chipher(message, step):
    """Return encrypted od decrypted message."""
    message = list(message.upper())
    for i, character in enumerate(message):
        ord_char = ord(character)
        if 65 <= ord_char <= 90:
            new_ord_char = ord_char + step
            if new_ord_char > 90:
                new_ord_char = 64 + (new_ord_char - 90)
            elif new_ord_char < 65:
                new_ord_char = 91 - (65 - new_ord_char)
            message[i] = chr(new_ord_char)
    return "".join(list(message))


if __name__ == "__main__":
    main()
