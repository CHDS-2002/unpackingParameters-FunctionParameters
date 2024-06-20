# Python 3.8

# os - library for working with the console
# random - library for working with random data

import os
import random

# Setting the font color of the console
os.system('COLOR B')

LEFT = 0  # LEFT - the left border
RIGHT = 20  # RIGHT - the right border
LEFT1 = ord('A')  # LEFT1 - character code 'A'
RIGHT1 = ord('Z')  # RIGHT1 - The code of the character 'Z'
LEFT2 = ord('a')  # LEFT2 - character code 'a'
RIGHT2 = ord('z')  # RIGHT2 - The code of the character 'z'
LEFT3 = ord('А')  # LEFT3 - The code of the symbol 'A'
RIGHT3 = ord('я')  # RIGHT3 - The code of the character 'Я'
MULTIPLIER = 100  # MULTIPLIER - multiplier


# get_info - a function for issuing a data type
def get_info():
    # info - list of data types
    info = [
        random.randint(LEFT, RIGHT),  # an integer
        random.randint(LEFT, RIGHT) * MULTIPLIER,  # floating point number
        complex(
            random.randint(LEFT, RIGHT),
            random.randint(LEFT, RIGHT)) * MULTIPLIER,  # an integer complex number
        complex(
            random.randint(LEFT, RIGHT),
            random.randint(LEFT, RIGHT)
        ),  # a complex integer
        bool(random.choice([0, 1])),
        ''.join([chr(random.choice([
            random.choice([
                random.randint(LEFT1, RIGHT1),
                random.randint(LEFT2, RIGHT2)]),
            ord(' '), ord(','), ord('.'), ord(';')
        ])) for _ in range(random.randint(LEFT, RIGHT))]),  # a string with English characters
        ''.join([chr(random.choice([
            random.randint(LEFT3, RIGHT3),
            ord(' '), ord(','), ord('.'), ord(';')
        ])) for _ in range(random.randint(LEFT, RIGHT))])  # a string with Russian characters
    ]

    return random.choice(info)  # data type output


# get_data - a function for issuing a data structure
def get_data():
    return random.choice([
        list(get_info() for _ in range(random.randint(LEFT, RIGHT))),  # list
        tuple(get_info() for _ in range(random.randint(LEFT, RIGHT))),  # The tuple
        {get_info(): get_info() for _ in range(random.randint(LEFT, RIGHT))},  # dictionary
        {get_info() for _ in range(random.randint(LEFT, RIGHT))}  # plenty
    ])


# print_params - function for output of parameters
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# Let's display the data on the screen
print('\nDATA OUTPUT\n')

print_params()
# They work
print_params(b=25)
print_params(c=[1, 2, 3])

SIZE = 3  # SIZE - number of parameters
a = ord('a')  # a - character code 'a'
c = ord('c')  # c - character code 'c'

values_list = [get_info() for _ in range(SIZE)]
# values_list - list
values_dict = {chr(s): get_data() for s in range(a, c)}
# values_dict - dictionary

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
print()

try:
    os.system('PAUSE')  # Stopping the program
    os.system('CLS')  # Clearing the console screen
except:
    os.system('CLS')  # Clearing the console screen
