"""
Caesar Cipher.
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.
"""

try:
    import pyperclip
except ImportError:
    pass  # If pyperclip is not installed, do nothing.


SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("""The Caesar cipher encrypts letters by shifting them over by a key number""")

# Let the user enter if they are encrypting or decrypting:
while True:  # Keep asking until the user enters  e or d.
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    response = input(">").lower()
    if response.startswith("e"):
        mode = "encrypt"
        break
    elif response.startswith("d"):
        mode = "decrypt"
        break
    print("Please enter the letter e or d.")

# Let the user enter key(step) to use
while True:
    max_key = len(SYMBOLS) - 1
    print(f"Please enter the key (0 to {max_key}) to use.")
    response = input(">").upper()

    if response.isdecimal() and (0 <= int(response) <= max_key):
        key = int(response)
        break

# Let the user enter the message to encrypt/decrypt
print("Enter the message:")
message = input(">").upper()

# Stores encrypted/decrypted message
translated = ""

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == "encrypt":
            num = num + key
        elif mode == "decrypt":
            pass
