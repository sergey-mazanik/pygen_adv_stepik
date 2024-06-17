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
