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


''' Треугольник Паскаля 2 '''

# def pascal_triangle(num):
#     lst = [[] for i in range(num)]
#     for i in range(num):
#         for j in range(i + 1):
#             if j < i:
#                 if j == 0:
#                     lst[i].append(1)
#                 else:
#                     lst[i].append(lst[i - 1][j] + lst[i - 1][j - 1])
#             elif j == i:
#                 lst[i].append(1)
#     return lst
#
#
# lst = pascal_triangle(int(input()))
# for i in lst:
#     print(*i)


''' Упаковка дубликатов '''

# lst1 = []
# lst2 = []
# for i in input().split():
#     if len(lst2) == 0:
#         lst2.append(i)
#     else:
#         if lst2[-1] == i:
#             lst2.append(i)
#         else:
#             lst1.append(lst2)
#             lst2 = []
#             lst2.append(i)
# if len(lst2) != 0:
#     lst1.append(lst2)
# print(lst1)


''' Разбиение на чанки '''

# lst = input().split()
# n = int(input())
# lst1 = []
# for i in range(0, len(lst), n):
#     lst1.append(lst[i:i + n])
# print(lst1)


''' Подсписки списка '''

# lst = input().split()
# lst1, lst2 = [], []
# for i in range(0, len(lst)):
#     for j in range(0, len(lst)):
#         lst1 = lst[j:i + j + 1]
#         if len(lst1) == i + 1:
#             lst2.append(lst1)
# print([[]] + lst2[::1])


''' Вывести матрицу 1 '''

# n = int(input())
# m = int(input())
# lst_final = []
# for i in range(n):
#     lst = []
#     for j in range(m):
#         lst.append(input())
#     lst_final.append(lst)
# for i in lst_final:
#     print(*i)


''' Вывести матрицу 2 '''

# n, m = int(input()), int(input())
# matrix = []
#
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(input())
#     matrix.append(row)
#
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end=' ')
#     print()
# print()
# for i in range(m):
#     for j in range(n):
#         print(matrix[j][i], end=' ')
#     print()


''' След матрицы '''

# n = int(input())
# matrix = []
# summa = 0
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
#
# for i in range(n):
#     summa += matrix[i][i]
# print(summa)


''' Больше среднего '''

# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
#
# for i in matrix:
#     avg = sum(i) / len(i)
#     count = 0
#     for j in i:
#         if j > avg:
#             count += 1
#     print(count)


''' Максимальный в области 1 '''

# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
#
# lst = []
# for row in range(n):
#     for col in range(n):
#         if row >= col:
#             lst.append(matrix[row][col])
# print(max(lst))


''' Максимальный в области 2 '''

# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
#
# lst = []
# for row in range(n):
#     for col in range(n):
#         if row == col or col == n - row - 1:
#             lst.append(matrix[row][col])
#         elif ((row > col) and (row < n - 1 - col)) or ((row < col) and (row > n - 1 - col)):
#             lst.append(matrix[row][col])
# print(max(lst))


''' Суммы четвертей '''

# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
#
# lst_up = []
# lst_down = []
# lst_left = []
# lst_right = []
# for row in range(n):
#     for col in range(n):
#         if (row > col) and (row < n - 1 - col):
#             lst_left.append(matrix[row][col])
#         elif (row < col) and (row > n - 1 - col):
#             lst_right.append(matrix[row][col])
#         elif (row > col) and (row > n - 1 - col):
#             lst_down.append(matrix[row][col])
#         elif (row < col) and (row < n - 1 - col):
#             lst_up.append(matrix[row][col])
# print(f'''Верхняя четверть: {sum(lst_up)}
# Правая четверть: {sum(lst_right)}
# Нижняя четверть: {sum(lst_down)}
# Левая четверть: {sum(lst_left)}
# ''')


''' Таблица умножения '''

# n = int(input())
# m = int(input())
# mult = []
# for row in range(n):
#     lst_col = []
#     for col in range(m):
#         lst_col.append(str(row * col).ljust(3))
#     mult.append(lst_col)
# for i in mult:
#     print(*i)


''' Максимум в таблице '''

# n = int(input())
# m = int(input())
# mult = []
# for _ in range(n):
#     mult.append(input().split())
#
# maximum = int(mult[0][0])
# for row in range(n):
#     for col in range(m):
#         if int(mult[row][col]) > maximum:
#             maximum = int(mult[row][col])
#
# for row in range(n):
#     for col in range(m):
#         if int(mult[row][col]) == maximum:
#             print(row, col)
#             quit()


''' Обмен столбцов '''

# n, m = int(input()), int(input())
# mult = []
# for _ in range(n):
#     mult.append(input().split())
# i, j = list(map(int, input().split()))
#
# for k in range(len(mult)):
#     mult[k][i], mult[k][j] = mult[k][j], mult[k][i]
#
# for i in mult:
#     print(*i)


''' Симметричная матрица '''

# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
#
# res = 'YES'
# for row in range(n):
#     for col in range(n):
#         if row != col:
#             if matrix[row][col] != matrix[col][row]:
#                 res = 'NO'
#                 break
# print(res)
