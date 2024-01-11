''' -------- Предикат делимости -------- '''
# def func(num1, num2):
#     return 'делится' if num1 % num2 == 0 else 'не делится'
#
#
# print(func(10, 2))
# print(func(5, 7))
# print(func(15, 15))


'''
Дополните приведенный код, используя списочный метод append(), чтобы список list1 имел вид:
list1 = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
'''

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)


'''
Дополните приведенный код, используя списочный метод extend(), чтобы список list1 имел вид:
list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
Подсписок для расширения  sub_list = ['h', 'i', 'j'].
'''

# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# sub_list = ['h', 'i', 'j']
# list1[2][1][2].extend(sub_list)
# print(list1)


'''
Дополните приведенный код, используя цикл for и встроенную функцию max(), 
чтобы он выводил максимальный элемент среди всех элементов вложенных списков списка list1.
'''

# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = 0
# for i in list1:
#     if max(i) > maximum:
#         maximum = max(i)
#
# print(maximum)


'''
Дополните приведенный код так, чтобы список list1 имел вид:
list1 = [[8, 7, 1], [102, 7, 9], [105, 106, 102], [103, 98, 99, 100], [3, 2, 1]]
'''

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# for i in list1:
#     i.reverse()
# print(list1)


'''
Дополните приведенный код так, чтобы он выводил единственное число: сумму всех чисел списка list1, 
разделённую на общее количество всех чисел.
'''

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
# for i in list1:
#     total += sum(i)
#     counter += len(i)
# print(total / counter)


''' -------- Список по образцу 1 -------- '''

# n = int(input())
# for _ in range(n):
#     lst1 = []
#     for j in range(1, n + 1):
#         lst1.append(j)
#     print(lst1)


''' -------- Список по образцу 2 -------- '''

# n = int(input())
# for i in range(1, n + 1):
#     print(list(range(1, i + 1)))


# n = int(input())
# s = []
# for i in range(1, n+1):
#     new_list = list()
#     for j in range(1, i+1):
#         new_list.append(j)
#     s.append(new_list)
# print(*s, sep="\n")

''' Треугольник Паскаля 1 '''

# n = int(input())
# triangle = []
#
# for i in range(n + 1):
#     triangle.append([1] + [0] * n)
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
# print(triangle[n])
