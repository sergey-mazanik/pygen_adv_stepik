# """ Содержимое файла """
#
# path = input()
# file = open(path, encoding='utf-8')
# for line in file.readlines():
#     print(line)
# file.close()


# """ Предпоследняя строка """
#
# file = open(input(), encoding='utf-8')
# lines = [line.strip() for line in file.readlines()]
# print(lines[-2])
# file.close()


# """ Случайная строка """
#
# from random import randint
#
#
# file = open('lines.txt', encoding='utf-8')
# lines = [line.strip() for line in file.readlines()]
# print(lines[randint(0, len(lines))])
# file.close()


# """ Сумма двух-1 """
#
# file = open('numbers.txt', encoding='utf-8')
# lines = [line.strip() for line in file.readlines()]
# print(int(lines[0]) + int(lines[1]))
# file.close()


# """ Сумма двух-2 """
#
# file = open('nums.txt', encoding='utf-8')
# lines = [line.strip() for line in file.readlines()]
# summa = 0
# for i in lines:
#     if i:
#         summa += int(i)
# print(summa)
# file.close()


# """ Общая стоимость """
#
# file = open('prices.txt', encoding='utf-8')
# summa = 0
# for line in file:
#     product = line.split()
#     summa += int(product[1]) * int(product[2])
# print(summa)
# file.close()


# with open('input.txt', encoding='utf-8') as file:
#     print('Repeat after me:', file.readline().strip())
#     for line in file:
#         print(line.strip() + '!')


# """ Переворот строки """
# with open('text.txt', encoding='utf-8') as file:
#     line = file.readline()
#     print(line[::-1])


# """ Обратный порядок """
# with open('data.txt', encoding='utf-8') as file:
#     lines = [line.strip() for line in file.readlines()]
#     lines.reverse()
#     print(*lines, sep='\n')


# """ Длинные строки """
# with open('lines.txt', encoding='utf-8') as file:
#     lines = [line.strip() for line in file.readlines()]
#     max_len = len(max(lines, key=len))
#     for line in lines:
#         if len(line) == max_len:
#             print(line)


# """ Сумма чисел в строках """
# with open('numbers.txt', encoding='utf-8') as file:
#     lines = [line.strip().split() for line in file.readlines()]
#     for line in lines:
#         summa = sum(map(int, line))
#         print(summa)


# """ Сумма чисел в файле """
# with open('nums.txt', encoding='utf-8') as file:
#     lines = [line.strip().split() for line in file.readlines()]
#     digits = ''
#     for line in lines:
#         for i in line:
#             for char in i:
#                 if char.isdigit():
#                     digits += char
#                 else:
#                     digits += ' '
#             digits += ' '
#     print(sum(int(i) for i in digits.split()))
