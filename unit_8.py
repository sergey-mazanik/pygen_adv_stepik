""" Тимур и его команда """

# n, m, k, x, y, z = [int(input()) for _ in range(6)]
# count = n + m + k + z - x - y
# print(count)

""" Книги на прочтение """

# n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
# s1 = -1 * (x - n - m) - t
# s2 = -1 * (y - m - k) - t
# s3 = -1 * (z - n - k) - t
# two_books = s1 + s2 + s3
# one_book = (n - s1 - s3 - t) + (m - s2 - s3 - t) + (k - s1 - s2 - t)
# no_books = a - t - two_books - one_book
#
# print(one_book, two_books, no_books, sep='\n')

# numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
# print(min(numbers) + max(numbers))

# numbers = {20, 6, 8, 18, 18, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 12, 8, 8, 10, 4, 2, 2, 2, 16, 20}
# average = sum(numbers) / len(numbers)
# print(average)

# numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
# my_set = {i ** 2 for i in numbers}
# print(sum(my_set))

# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
# for fruit in sorted(fruits, reverse=True):
#     print(fruit)

# print(len(set(input())))

# str = input()
# print('YES' if len(str) == len(set(str)) else 'NO')

# str1, str2 = [input() for _ in range(2)]
# print('YES' if len(set(str1 + str2)) == 10 else 'NO')

# str1, str2 = [input() for _ in range(2)]
# print('YES' if sorted(set(str1)) == sorted(set(str2)) else 'NO')

# lst = input().split()
# print('YES' if set(lst[0]) == set(lst[1]) == set(lst[2]) else 'NO')

# lst = []
# for i in range(int(input())):
#     lst.append(len(set(input().lower())))
# print(*lst, sep='\n')

# my_set = set()
# for _ in range(int(input())):
#     my_set.update(input().lower())
# print(len(my_set))

# words = [word.lower().strip('.,;:-?!') for word in input().split()]
# print(len(set(words)))

# lst = list(map(int, input().split()))
# my_set = set()
# for i in lst:
#     if i in my_set:
#         print('YES')
#     else:
#         print('NO')
#         my_set.add(i)
