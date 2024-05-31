# def matrix(n=1, m=None, value=0):
#     if m is None:
#         m = n
#     mat = [[value] * m for _ in range(n)]
#     return mat


# def count_args(*args):
#     return len(args)


# def sq_sum(*args):
#     return sum(i ** 2 for i in args)


# def mean(*args):
#     lst = [i for i in args if type(i) in (int, float)]
#     if len(lst) > 0:
#         return sum(lst) / len(lst)
#     else:
#         return 0.0


# def greet(name, *args):
#     if args:
#         return f'Hello, {name} and {" and ".join(args)}!'
#     else:
#         return f'Hello, {name}!'


# def print_products(*args):
#     products = []
#     for i in args:
#         if isinstance(i, str) and i != '':
#             products.append(i)
#     if products:
#         for i in range(len(products)):
#             print(f'{i + 1}) {products[i]}')
#     else:
#         print('Нет продуктов')


# def info_kwargs(**kwargs):
#     for k, v in sorted(kwargs.items()):
#         print(f'{k}: {v}')


# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34),
#            (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4),
#            (90, 1, -45, -21)]
#
#
# def comparator(item):
#     return sum(item) / len(item)
#
#
# print(min(numbers, key=comparator), max(numbers, key=comparator), sep='\n')


# def foo(x):
#     return (x[0] ** 2 + x[1] ** 2) ** 0.5
#
#
# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
# points.sort(key=foo)
# print(points)


# def foo(x):
#     return max(x) + min(x)
#
#
# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99),
#            (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
# numbers.sort(key=foo)
# print(numbers)


# def foo(x, n=input()):
#     return x[int(n)-1]
#
#
# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
#             ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
#
# athletes.sort(key=foo)
# for i in athletes:
#     print(*i)

# import math
#
#
# def f1(x):
#     return x ** 2
#
#
# def f2(x):
#     return x ** 3
#
#
# def f3(x):
#     return x ** 0.5
#
#
# def f4(x):
#     return abs(x)
#
#
# def f5(x):
#     return math.sin(x)
#
#
# commands = {'квадрат': f1, 'куб': f2, 'корень': f3, 'модуль': f4, 'синус': f5}
# n = int(input())
# command = input()
# print(commands[command](n))


# def comparator(x):
#     summa = 0
#     for i in x:
#         summa += int(i)
#     return summa
#
#
# lst = input().split()
# lst.sort(key=comparator)
# print(*lst)


# def comparator(x):
#     return sum([int(i) for i in str(x)])
#
#
# lst = sorted([int(i) for i in input().split()])
# lst.sort(key=comparator)
# print(lst)

