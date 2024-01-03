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


# -------- Больше предыдущего  ---------

# lst = list(map(int, input().split()))
# count = 0
# for i in range(1, len(lst)):
#     if lst[i] > lst[i-1]:
#         count += 1
# print(count)
