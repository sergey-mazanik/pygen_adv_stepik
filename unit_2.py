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
