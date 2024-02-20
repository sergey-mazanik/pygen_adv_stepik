# import random
#
# random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел
# for _ in range(10):
#     print(random.randint(1, 100))


# import random
#
# n = int(input())
# for _ in range(n):
#     print(random.choice(['Орел', 'Решка']))


# import random
#
# n = int(input())
# for _ in range(n):
#     print(random.randint(1, 6))


# import random
#
# length = int(input())
# password = ''
# for _ in range(length):
#     up_or_low = random.randint(0, 1)
#     if up_or_low == 0:
#         password += chr(random.randint(65, 90))
#     else:
#         password += chr(random.randint(97, 122))
#
# print(password)


# import random
#
# lst = []
# for _ in range(7):
#     lst.append(random.randint(1, 49))
# print(*sorted(lst))


