import random
from vars import *


def rand_code(characters=5):
    """
    Returns a random string containing alphabets and numbers
    Default number of characters: 5
    """
    code_list = [alphabets, numbers]
    i = 0
    code = ''
    while i < characters:
        choice = random.choice(code_list)
        code = code + str(random.choice(choice))
        i += 1
    return code


def alphabet_code(characters=5):
    """
    Returns a string containing random alphabets (Both lower and upper case)
    Default number of characters: 5
    """
    i = 0
    code = ''
    while i < characters:
        code = code + str(random.choice(alphabets))
        i += 1
    return code


def number_code(characters=5):
    """
    Returns a string containing random numbers
    Default number of characters: 5
    """
    i = 0
    code = ''
    while i < characters:
        code = code + str(random.choice(numbers))
        i += 1
    return code


print(rand_code())
print(alphabet_code())
print(number_code())
