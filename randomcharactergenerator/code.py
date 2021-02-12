import random


def rand_code(characters=5):
    """
    Returns a random string containing alphabets and numbers
    Default number of characters: 5
    """
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a',
                 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                 't', 'u', 'v', 'w', 'x', 'y', 'r']

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    code_list = [alphabets, numbers]
    i = 0
    code = ''
    while i < characters:
        choice = random.choice(code_list)
        code = code + str(random.choice(choice))
        i += 1
    return code


def alphabet_code(characters=5):
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a',
                 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                 't', 'u', 'v', 'w', 'x', 'y', 'r']
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
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
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
