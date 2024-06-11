# def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
#     return f'''To: {mail}
# Приветствую, {name}!
# Вам назначен экзамен, который пройдет {date}, в {time}.
# По адресу: {place}.
# Экзамен будет проводить {teacher} в кабинете {number}.
# Желаем удачи на экзамене!'''
#
#
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря',
#                       '12:00', 'Часова 23, корпус 2'))
# print()
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00',
#                       'Часова 23, корпус 2', 'Василь Ярошевич', 23))
import struct


# """ Pretty print """
#
#
# def pretty_print(data: list, side='-', delimiter='|'):
#     lst = []
#     for i in range(len(data)):
#         lst.append(delimiter + " " + str(data[i]))
#     c = " ".join(lst) + " " + delimiter
#     s = " " + side*(len(c)-2) + " "
#     b = [s, c, s]
#     print('\n'.join(b))
#
#
# pretty_print([1, 2, 10, 23, 123, 3000])
# pretty_print(['abc', 'def', 'ghi', '12345'])
# pretty_print(['abc', 'def', 'ghi'], side='*')
# pretty_print(['abc', 'def', 'ghi'], delimiter='#')
# pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')


# def concat(*args, sep=' '):
#     return sep.join(map(str, args))
#
#
# print(concat('hello', 'python', 'and', 'stepik'))
# print(concat('hello', 'python', 'and', 'stepik', sep='*'))
# print(concat('hello', 'python', sep='()()()'))
# print(concat('hello', sep='()'))
# print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))


# from functools import reduce
#
#
# def product_of_odds(data):
#     odd_lst = filter(lambda x: x % 2 == 1, data)
#     return reduce(lambda x, y: x * y, odd_lst, 1)
#
#
# print(product_of_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# words = 'the world is mine take a look what you have started'.split()
#
# print(*map(lambda x: f'"{x}"', words))


# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
# print(*filter(lambda x: str(x) != str(x)[::-1], numbers))


# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,),
#            (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
#
# sorted_numbers = sorted(numbers, key=lambda x: sum(x) / len(x), reverse=True)
#
# print(sorted_numbers)


# def call(func, *args):
#     return func(*args)
#
#
# def mul7(x):
#     return x * 7
#
#
# def add2(x, y):
#     return x + y
#
#
# def add3(x, y, z):
#     return x + y + z
#
#
# print(call(mul7, 10))
# print(call(add2, 2, 7))
# print(call(add3, 10, 30, 40))
# print(call(bool, 0))


# def compose(f, g):
#     def wrapper(h):
#         return f(g(h))
#     return wrapper
#
#
# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
#
# print(compose(mul7, add3)(1))
# print(compose(add3, mul7)(2))
# print(compose(mul7, str)(3))
# print(compose(str, mul7)(5))


# def arithmetic_operation(operation):
#     return {
#     '+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y
#     }[operation]
#
#
# add = arithmetic_operation('+')
# div = arithmetic_operation('/')
# print(add(10, 20))
# print(div(20, 5))


# print(*sorted(input().split(), key=lambda x: x.lower()))


# def gematry(word: str):
#     upper_word = word.upper()
#     gem = sum([ord(i) - ord('A') for i in upper_word])
#     return gem
#
#
# n = int(input())
# lst = [input() for _ in range(n)]
# lst.sort()
#
# print(*sorted(lst, key=gematry), sep='\n')


# def ip(s: str):
#     lst = [int(i) for i in s.split('.')]
#     return lst[0] * 256 ** 3 + lst[1] * 256 ** 2 + lst[2] * 256 + lst[3]
#
#
# n = int(input())
# lst = [input() for _ in range(n)]
# print(*sorted(lst, key=ip), sep='\n')
