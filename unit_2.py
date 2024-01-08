# -------- На easy ---------

# a, b = int(input()), int(input())
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print((a ** 10 + b ** 10) ** 0.5)


# -------- Индекс массы тела ---------

# weight, height = float(input()), float(input())
# index_w_h = weight / (height * height)
# if 18.5 <= index_w_h <= 25:
#     print('Оптимальная масса')
# elif index_w_h < 18.5:
#     print('Недостаточная масса')
# elif index_w_h > 25:
#     print('Избыточная масса')


# -------- Стоимость строки ---------

# st = input()
# sum_kop = len(st) * 60
# print(sum_kop)
# print(f'{sum_kop // 100} р. {sum_kop % 100} коп.')


# -------- Количество слов ---------

# print(len(input().split()))


# -------- Зодиак ---------

# year = int(input())
# animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
# print(animals[year % 12])


# -------- Переворот числа ---------

# st = input()
# if len(st) == 6:
#     print(int(st[:1] + st[-1:0:-1]))
# else:
#     print(int(st[::-1]))


# -------- Standard American Convention ---------

# st = int(input())
# print(f'{st:,}')


# -------- Задача Иосифа Флавия  ---------

# n = int(input())
# k = int(input())
# num = 0
# for i in range(1, n + 1):
#     num = (num + k) % i
# print(num + 1)


# -------- Координатные четверти  ---------

# n = int(input())
# first = 0
# second = 0
# third = 0
# fourth = 0
# for i in range(n):
#     x, y = map(int, input().split())
#     if x > 0 and y > 0:
#         first += 1
#     elif x < 0 and y > 0:
#         second += 1
#     elif x < 0 and y < 0:
#         third += 1
#     elif x > 0 and y < 0:
#         fourth += 1
# print(f'''Первая четверть: {first}
# Вторая четверть: {second}
# Третья четверть: {third}
# Четвертая четверть: {fourth}''')


# -------- Больше предыдущего ---------

# lst = list(map(int, input().split()))
# count = 0
# for i in range(1, len(lst)):
#     if lst[i] > lst[i-1]:
#         count += 1
# print(count)


# -------- Назад, вперёд и наоборот ---------

# lst = list(map(int, input().split()))
# for i in range(0, len(lst) - 1, 2):
#     lst[i], lst[i + 1] = lst[i + 1], lst[i]
# print(*lst)


# -------- Сдвиг в развитии ---------

# lst = list(map(int, input().split()))
# print(lst[-1], *lst[:-1])


# -------- Различные элементы ---------

# lst = list(map(int, input().split()))
# lst_avg = []
# for i in range(len(lst)):
#     if lst[i] not in lst_avg:
#         lst_avg.append(lst[i])
# print(len(lst_avg))


# -------- Произведение чисел ---------

# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))
# multi = int(input())
# flag = False
# for i in range(len(lst)):
#     for j in range(len(lst)):
#         if i != j:
#             if lst[i] * lst[j] == multi:
#                 flag = True
# print('ДА' if flag else 'НЕТ')


# -------- Камень, ножницы, бумага ---------

# tim = input()
# rus = input()
# k = 'камень'
# n = 'ножницы'
# b = 'бумага'
# if tim == rus:
#     print('ничья')
# elif (tim == k and rus == n) or (tim == n and rus == b) or (tim == b and rus == k):
#     print('Тимур')
# elif (tim == k and rus == b) or (tim == n and rus == k) or (tim == b and rus == n):
#     print('Руслан')

# -------- Камень, ножницы, бумага, ящерица, Спок ---------

# a, b = input(), input()
# mass = ['ножницыбумага', 'ножницыящерица', 'бумагакамень', 'бумагаСпок', 'каменьящерица', 'каменьножницы',
#         'ящерицаСпок', 'ящерицабумага', 'Спокножницы', 'Споккамень']
# if a == b:
#     print('ничья')
# elif a + b in mass:
#     print('Тимур')
# else:
#     print('Руслан')


# -------- Орел и решка ---------

# lst = list(map(str, input().split('О')))
# print(len(max(lst)))


# -------- Кремниевая долина ---------
# n = int(input())
# line_number = 0
# count = 0
# lst = []
# for i in range(n):
#     line_number += 1
#     line = input()
#     first_letter = line.find('a')
#     second_letter = line.find('n', first_letter)
#     third_letter = line.find('t', second_letter)
#     forth_letter = line.find('o', third_letter)
#     fifth_letter = line.find('n', forth_letter)
#     if line[first_letter] == 'a' and line[second_letter] == 'n' and line[third_letter] == 't' and line[
#         forth_letter] == 'o' and line[fifth_letter] == 'n':
#         lst.append(line_number)
# print(*lst)


# -------- Роскомнадзор запретил букву а ---------

# name = input()
# s = name + ' запретил букву'
# alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
#             'х', 'ц',
#             'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
# for i in range(len(alphabet)):
#     letter = alphabet[i]
#     if letter in s:
#         if i != '':
#             print(s, end=' ')
#         s = s.replace(letter, '').replace('  ', ' ').strip()
#         print(letter)
