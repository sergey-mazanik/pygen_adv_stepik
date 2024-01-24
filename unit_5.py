''' Каждый n-ый элемент '''

# lst = input().split()
# n = int(input())
# new_list = []
# for i in range(n):
#     new_list.append(lst[i::n])
# print(new_list)


''' Максимальный в области 2 '''

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# sec_matrix = []
# for i in range(n):
#     for j in range(n):
#         if i >= n - 1 - j:
#             sec_matrix.append(matrix[i][j])
#
# print(max(sec_matrix))


''' Транспонирование матрицы '''

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# new_matrix = []
# for col in range(n):
#     new_row = []
#     for row in range(n):
#         new_row.append(matrix[row][col])
#     new_matrix.append(new_row)
#
# for i in new_matrix:
#     print(*i)


''' Снежинка '''

# n = int(input())
# matrix = [['.' for _ in range(n)] for _ in range(n)]
#
# for r in range(n):
#     for c in range(n):
#         if r == c or c == n - r - 1 or r == n // 2 or c == n // 2:
#             matrix[r][c] = '*'
#
# for i in matrix:
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
#         if matrix[row][col] != matrix[n-col-1][n-row-1]:
#             res = 'NO'
#             break
# print(res)


''' Латинский квадрат '''

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# new_matrix = []
# for col in range(n):
#     new_row = []
#     for row in range(n):
#         new_row.append(matrix[row][col])
#     new_matrix.append(new_row)
# check_values = list(range(1, n + 1))
#
# for r in matrix:
#     if sorted(r) != check_values:
#         print('NO')
#         quit()
#
# for r in new_matrix:
#     if sorted(r) != check_values:
#         print('NO')
#         quit()
#
# print('YES')


''' Ходы ферзя '''

# start = input()
# matrix = [['.' for _ in range(8)] for _ in range(8)]  # b6
# pos_x, pos_y = 8-int(start[1]), ord(start[0])-97
# matrix[pos_x][pos_y] = 'Q'
#
# for r in range(8):
#     for c in range(8):
#         if abs(pos_x - r) == abs(pos_y - c) or pos_x == r or pos_y == c:
#             matrix[r][c] = '*'
# matrix[pos_x][pos_y] = 'Q'
#
# for i in range(8):
#     print(*matrix[i])


''' Диагонали, параллельные главной '''

# n = int(input())
# matrix = [[0] * n for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             if k == i - j or k == j - i:
#                 matrix[i][j] = k
#
# for i in matrix:
#     print(*i)
