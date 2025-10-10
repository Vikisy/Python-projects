# Random password generator (length between 8 and 16)

from random import *
from string import *

def password ():
    if length < 8:
        raise ValueError("Password length should be at least 8")
    if length > 16:
        raise ValueError("Password length should not be greater than 16")

    # Characters to include
    lower = choice(ascii_lowercase)
    upper = choice(ascii_uppercase)
    digit = choice(digits)
    special = choice(punctuation)

    # Fill the rest with random characters
    r_chars = ascii_letters + digits + punctuation
    rest = [choice(r_chars) for _ in range(length - 4)]

    # group and shuffle
    generate_password = list(lower + upper + digit + special) + rest
    shuffle(generate_password)

    return ''.join(generate_password)

if __name__ == "__main__":
    name = input("What is your first name? ")
    length = int(input("Enter password length (from 8 to 16): "))
    print("Dear",name+',',"your new password is:", password())
    print("Kindly keep safe")