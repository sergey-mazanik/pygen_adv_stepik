# my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa',
#            10.12: [1, 2, 3], 99.0: {9, 0, 1}}
# print(max(my_dict) + min(my_dict))

# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# lst = []
# for user in users:
#     if user['phone'][-1] == '8':
#         lst.append(user['name'])
# print(*sorted(lst))

# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# lst = []
# for user in users:
#     if len(user) < 3 or user['email'] == '':
#         lst.append(user['name'])
# print(*sorted(lst))

# numbers_dict = {
#     "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven",
#     "8": "eight", "9": "nine"
# }
# num = input()
# for i in range(len(num)):
#     print(numbers_dict[num[i]], end=' ')

# courses = {'CS101': '3004, Хайнс, 8:00',
#            'CS102': '4501, Альварадо, 9:00',
#            'CS103': '6755, Рич, 10:00',
#            'NT110': '1244, Берк, 11:00',
#            'CM241': '1411, Ли, 13:00'
#            }
# my_str = input()
# if my_str in courses:
#     print(f'{my_str}: {courses[my_str]}')

# d = {
#     "1": ".,?!:",
#     "2": "ABC",
#     "3": "DEF",
#     "4": "GHI",
#     "5": "JKL",
#     "6": "MNO",
#     "7": "PQRS",
#     "8": "TUV",
#     "9": "WXYZ",
#     "0": " "
# }
# my_str = input().upper()
# for i in range(len(my_str)):
#     for k, v in d.items():
#         if my_str[i] in v:
#             index = list(v).index(my_str[i])
#             print(k * (index+1), end='')

# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
#          '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
#          '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# morse_dict = dict(zip(letters, morse))
# my_str = input().upper()
# lst = []
# for i in my_str:
#     if i in morse_dict:
#         lst.append(morse_dict[i])
# print(*lst)

# result = {}
# for i in range(1, 16):
#     result[i] = i ** 2
# print(result)

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
# result = {}
# for key in dict1.keys():
#     if key in dict2:
#         value = dict1[key] + dict2[key]
#         result[key] = value
#     else:
#         result[key] = dict1[key]
#
# for key in dict2.keys():
#     if key not in result:
#         result[key] = dict2[key]
# print(result)

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
# result = dict1.copy()
# for key, value in dict2.items():
#     result[key] = result.get(key, 0) + value

# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# result = {}
# for i in text:
#     result[i] = result.get(i, 0) + 1
# print(result)

# s = ('orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana'
#      ' orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon'
#      ' strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit'
#      ' barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit'
#      ' strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot'
#      ' barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley'
#      ' lime grapefruit pomegranate barley')
# result = {}
# lst = []
# for i in s.split():
#     result[i] = result.get(i, 0) + 1
# max_num = max(result.values())
# for key, value in result.items():
#     if value == max_num:
#         lst.append(key)
# print(min(lst))

# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
# result = {}
# for i in pets:
#     result.setdefault(i[1:], []).append(i[0])
# print(result)

# lst = [i.strip('().,;:-?!') for i in input().lower().split()]
# result = {}
# for i in lst:
#     result[i] = result.get(i, 0) + 1
# min_num = 1000
# lst_res = []
# for key, value in sorted(result.items(), key=lambda x: x[1]):
#     # print(f'{key}: {value}')
#     if value <= min_num:
#         lst_res.append(key)
#         min_num = value
# print(min(lst_res))

# lst = []
# for i in input().split():
#     if i not in lst:
#         print(i, end=' ')
#     else:
#         print(f'{i}_{lst.count(i)}', end=' ')
#     lst.append(i)

""" Словарь программиста """

# n = int(input())
# my_dict = {}
# for i in range(n):
#     lst = input().split(': ')
#     my_dict[lst[0].upper()] = lst[1]
# print(my_dict)
#
# m = int(input())
# for i in range(m):
#     s = input().upper()
#     if s in my_dict:
#         print(my_dict[s])
#     else:
#         print('Не найдено')

""" Анаграммы 1 """

# s1, s2 = input(), input()
# dict1 = {}
# dict2 = {}
# for i in s1:
#     dict1[i] = dict1.get(i, 0) + 1
# for i in s2:
#     dict2[i] = dict2.get(i, 0) + 1
#
# print('YES' if dict1 == dict2 else 'NO')

# lst1 = list(map(str, input().split()))
# lst2 = list(map(str, input().split()))
# dict1 = {}
# dict2 = {}
# for i in lst1:
#     for j in i.lower():
#         if j.isalpha():
#             dict1[j.lower()] = dict1.get(j.lower(), 0) + 1
# for i in lst2:
#     for j in i:
#         if j.isalpha():
#             dict2[j.lower()] = dict2.get(j.lower(), 0) + 1
#
# print('YES' if dict1 == dict2 else 'NO')

""" Словарь синонимов """

# my_dict = {}
# for i in range(int(input())):
#     lst = [i for i in input().split()]
#     my_dict[lst[0]], my_dict[lst[1]] = lst[1], lst[0]
# print(my_dict[input()])

""" Страны и города """

# my_dict = {}
# for _ in range(int(input())):
#     lst = [i for i in input().split()]
#     my_dict[lst[0]] = lst[1:]
# find_city = [input() for i in range(int(input()))]
# for i in find_city:
#     for key, value in my_dict.items():
#         if i in value:
#             print(key)

""" Телефонная книга """

# my_dict = {}
# for _ in range(int(input())):
#     lst = [i.lower() for i in input().split()]
#     my_dict.setdefault(lst[1], []).append(lst[0])
# print(my_dict)
# for _ in range(int(input())):
#     # print(*my_dict.get(input().lower(), ['абонент не найден']))
#     name = input().lower()
#     if name in my_dict.keys():
#         print(*my_dict.get(name, 'абонент не найден'))
#     else:
#         print('абонент не найден')

""" Секретное слово """

# my_str = input()
# dict_str = {}
# for i in my_str:
#     dict_str[i] = dict_str.get(i, 0) + 1
# my_dict = {}
# for _ in range(int(input())):
#     letter, count = input().split(': ')
#     my_dict[count] = letter
# new_str = ''
# for i in my_str:
#     n = dict_str[i]
#     new_str += my_dict[str(n)]
# print(new_str)

# my_str = input()
# my_dict = {}
# for i in range(int(input())):
#     k, v = input().split(': ')
#     my_dict[v] = k
# dict_str = {x: my_str.count(x) for x in my_str}
# new_str = ''
# for letter in my_str:
#     n = dict_str[letter]
#     new_str += my_dict[str(n)]
# print(new_str)


# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
# result = {i: numbers[i] ** 2 for i in range(len(numbers))}
# print(result)


# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange',
#           'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber',
#           'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None,
#           'c22': 'Sand', 'c23': None}
# result = {k: v for k, v in colors.items() if v is not None}
# print(result)

# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62,
#                     'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654,
#                     'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271,
#                     'anna': 55, 'madlen': 876}
# result = {k: v for k, v in favorite_numbers.items() if 9 < v < 100}
# print(result)


# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
#           9: 'September', 10: 'October', 11: 'November', 12: 'December'}
# result = {v: k for k, v in months.items()}
# print(result)


# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
# result = {int(k): v for k, v in [i.split(':') for i in s.split()]}
# print(result)


# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
# result = {k: [v for v in range(1, k + 1) if k % v == 0] for k in numbers}
# print(result)
