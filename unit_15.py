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


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def round2(x):
#     return round(x, 2)
#
#
# numbers = [
#     3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546
# ]
# print(*map(round2, numbers), sep='\n')


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# def num_is_three(x):
#     return len(str(x)) == 3
#
#
# def div_three_is(x):
#     return x % 5 == 2
#
#
# def cube(x):
#     return x ** 3
#
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462,
#            815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155,
#            230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669,
#            105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351,
#            1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
#
# num_3 = filter(num_is_three, numbers)
# num_div = filter(div_three_is, num_3)
# cubes = map(cube, num_div)
# print(*cubes, sep='\n')


# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
#
#
# def foo(x, y):
#     return x + y ** 2
#
#
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35,
#            11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36,
#            72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35,
#            7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
# print(reduce(foo, numbers, 0))


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# def cond(x):
#     return len(str(abs(x))) == 2 and x % 7 == 0
#
#
# def square(x):
#     return x ** 2
#
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270,
#            219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35,
#            152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5,
#            187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35,
#            211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2,
#            79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234,
#            10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
# print(sum(map(square, filter(cond, numbers))))


# def func_apply(func, items):
#     return list(map(func, items))
#
#
# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7


# from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(lambda num: round((num ** 2), 1), floats))
# filter_result = list(filter(lambda name: len(name) > 4 and name == name[::-1], words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)


# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
#
# new_data = list(filter(lambda x: x[1] > 10000000, list(filter(lambda x: x[2] == 'primary', data))))
# new_data.sort(key=lambda x: x[0])
# cities = [i[0] for i in new_data]
# print(f'Cities: {", ".join(cities)}')


# func = lambda x: True if x % 19 == 0 or x % 13 == 0 else False


# func = lambda x: x[0] in 'Aa' and x[-1] in 'Aa'


# is_non_negative_num = lambda x: x.replace('.', '').isdigit() and x.count('.') < 2


# is_num = lambda x: x.replace('.', '').replace('-', '', 1).isdigit() and x.count('.') < 2 and x.rfind('-') <= 0


# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able',
#          'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound',
#          'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday',
#          'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry',
#          'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
# sort_word = list(sorted(filter(lambda s: len(s) == 6, words)))
# print(' '.join(sort_word))


# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80,
#            93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57,
#            53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94,
#            37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
# even_numbers = list(filter(lambda x: not (x % 2 != 0 and x > 47), numbers))
# result = list(map(lambda x: x // 2 if x % 2 == 0 else x, even_numbers))
# print(*result)


# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'),
#         (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'),
#         (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'),
#         (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
# data.sort(key=lambda x: x[-1][-1], reverse=True)
# for i in data:
#     print(f'{i[1]}: {i[0]}')


# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг',
#         'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид',
#         'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
# data.sort()
# data.sort(key=lambda x: len(x))
# print(*data)


# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday',
#               'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271,
#               2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides',
#               'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent',
#               'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet',
#               859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth',
#               'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage',
#               'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552,
#               1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
# print(max(filter(lambda x: isinstance(x, int), mixed_list)))


# mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76,
#               70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort',
#               13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80,
#               'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon',
#               'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt',
#               'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]
# lst = sorted(mixed_list, key=lambda x: str(x))
# print(*lst)


# print(*map(lambda x: 255 - x, map(int, input().split())))


""" Значение многочлена 🌶️ """

# from functools import reduce
#
#
# def evaluate(coefficients, x):
#     lst = list(range(len(coefficients))[::-1])
#     result = list(map(lambda a, b: a * x ** b, coefficients, lst))
#     print(reduce(lambda a, b: a + b, result))
#
#
# evaluate(list(map(int, input().split())), int(input()))
