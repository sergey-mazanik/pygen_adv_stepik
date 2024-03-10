# import random
#
# random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел
# for _ in range(10):
#     print(random.randint(1, 100))
import string
# import random
#
# n = int(input())
# for _ in range(n):
#     print(random.choice(['Орел', 'Решка']))


# import random
#
# n = int(input())
# for _ in range(n):
#     print(random.randint(1, 6))


# import random
#
# length = int(input())
# password = ''
# for _ in range(length):
#     up_or_low = random.randint(0, 1)
#     if up_or_low == 0:
#         password += chr(random.randint(65, 90))
#     else:
#         password += chr(random.randint(97, 122))
#
# print(password)


# import random
#
# lst = []
# for _ in range(7):
#     lst.append(random.randint(1, 49))
# print(*sorted(lst))


# import random
#
#
# def generate_ip():
#     ip = ['192', '168', str(random.choice(list(range(1, 256)))), str(random.choice(list(range(1, 256))))]
#     return '.'.join(ip)


# from random import choice
#
#
# def generate_index():
#     letter = string.ascii_uppercase
#     numbers = list(range(0, 100))
#     return (choice(letter) + choice(letter) + str(choice(numbers)) + '_' + str(choice(numbers)) + choice(letter) +
#             choice(letter))


# from random import shuffle
#
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
# for i in matrix:
#     shuffle(i)


# from random import randint
#
# print(*[randint(1000000, 9999999) for i in range(100)], sep='\n')


# from random import shuffle
#
# word = list(input())
# shuffle(word)
# print(''.join(word))


# from random import sample
#
# lst = list(range(1, 76))
# numbers_list = sample(lst, 25)
# bingo_matrix = [[str(numbers_list.pop()).ljust(3) for _ in range(5)] for _ in range(5)]
# bingo_matrix[2][2] = str(0).ljust(3)
# [print(*row, sep='') for row in bingo_matrix]


# from random import shuffle
#
# lst = [input() for _ in range(int(input()))]
# shuffle(lst)
# for i in range(len(lst)):
#     print(lst[i], '-', lst[i - 1])


# from string import ascii_letters, digits
# from random import choice
#
#
# def generate_password(length):
#     letter = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))
#     password = ''
#     for _ in range(length):
#         password += choice(letter)
#     return password
#
#
# def generate_passwords(count, length):
#     for _ in range(count):
#         print(generate_password(length))
#
#
# n, m = int(input()), int(input())
# generate_passwords(n, m)


# from string import ascii_uppercase, ascii_lowercase, digits, ascii_letters
# from random import choice, shuffle
#
# LETTER = {'EN': [x for x in ascii_uppercase if x not in 'OI'],
#           'en': [x for x in ascii_lowercase if x not in 'ol'],
#           'dig': [x for x in digits if x not in '01']}
# letter = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))
#
#
# def generate_password(length):
#     password = choice(LETTER['EN']) + choice(LETTER['en']) + choice(LETTER['dig'])
#     for _ in range(length - 3):
#         password += choice(letter)
#     password = list(password)
#     shuffle(password)
#     return ''.join(password)
#
#
# def generate_passwords(count, length):
#     for _ in range(count):
#         print(generate_password(length))
#
#
# n, m = int(input()), int(input())
# generate_passwords(n, m)

