# Python 3.8

# os - библиотека для работы с консолью
# random - библиотека для работы со случайными данными

import os
import random

# Зададим цвет шрифта консоли
os.system('COLOR B')

LEFT = 0  # LEFT - левая граница
RIGHT = 20  # RIGHT - правая граница
LEFT1 = ord('A')  # LEFT1 - код символа 'A'
RIGHT1 = ord('Z')  # RIGHT1 - код символа 'Z'
LEFT2 = ord('a')  # LEFT2 - код символа 'a'
RIGHT2 = ord('z')  # RIGHT2 - код символа 'z'
LEFT3 = ord('А')  # LEFT3 - код символа 'А'
RIGHT3 = ord('я')  # RIGHT3 - код символа 'я'
MULTIPLIER = 100  # MULTIPLIER - множитель


# get_info - функция для выдачи типа данных
def get_info():
    # info - список типов данных
    info = [
        random.randint(LEFT, RIGHT),  # целое число
        random.randint(LEFT, RIGHT) * MULTIPLIER,  # число с плавающей точкой
        complex(
            random.randint(LEFT, RIGHT),
            random.randint(LEFT, RIGHT)) * MULTIPLIER,  # комплексное число
        complex(
            random.randint(LEFT, RIGHT),
            random.randint(LEFT, RIGHT)
        ),  # целое комплексное число
        bool(random.choice([0, 1])),
        ''.join([chr(random.choice([
            random.choice([
                random.randint(LEFT1, RIGHT1),
                random.randint(LEFT2, RIGHT2)]),
            ord(' '), ord(','), ord('.'), ord(';')
        ])) for _ in range(random.randint(LEFT, RIGHT))]),  # строка с английскими символами
        ''.join([chr(random.choice([
            random.randint(LEFT3, RIGHT3),
            ord(' '), ord(','), ord('.'), ord(';')
        ])) for _ in range(random.randint(LEFT, RIGHT))])  # строка с русскими символами
    ]

    return random.choice(info)  # вывод типа данных


# get_data - функция для выдачи структуры данных
def get_data():
    return random.choice([
        list(get_info() for _ in range(random.randint(LEFT, RIGHT))),  # список
        tuple(get_info() for _ in range(random.randint(LEFT, RIGHT))),  # кортеж
        {get_info(): get_info() for _ in range(random.randint(LEFT, RIGHT))},  # словарь
        {get_info() for _ in range(random.randint(LEFT, RIGHT))}  # множество
    ])


# print_params - функция для вывода параметров
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# Выведем данные на экран
print('\nВЫВОД ДАННЫХ\n')

print_params()
# работают
print_params(b=25)
print_params(c=[1, 2, 3])

SIZE = 3  # SIZE - количество параметров
a = ord('a')  # a - код символа 'a'
c = ord('c')  # c - код символа 'c'

values_list = [get_info() for _ in range(SIZE)]
# values_list - список
values_dict = {chr(s): get_data() for s in range(a, c)}
# values_dict - словарь

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
print()

try:
    os.system('PAUSE')  # Останавливаем работу программы
    os.system('CLS')  # Очищаем экран консоли
except:
    os.system('CLS')  # Очищаем экран консоли
