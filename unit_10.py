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


