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

# lst1 = list(map(int, input().split()))
# lst2 = list(map(int, input().split()))
# print(len((set(lst1) & set(lst2))))

# # set1 = set(int(i) for i in input().split())
# # set2 = set(int(i) for i in input().split())
# lst1 = list(map(int, input().split()))
# lst2 = list(map(int, input().split()))
# my_set = set(lst1) & set(lst2)
# for i in sorted(my_set):
#     print(i, end=' ')

# set1 = set(int(i) for i in input().split())
# set2 = set(int(i) for i in input().split())
# print(*sorted(set1 - set2))

# n = int(input())
# set1 = set(input())
# for i in range(n - 1):
#     set1 &= set(input())
# print(*sorted(set1))

# print('NO' if set(input()).isdisjoint(set(input())) else 'YES')

# a, b = set(input()), set(input())
# print('YES' if a.issuperset(b) else 'NO')
# print('YES' if set(input()).issuperset(set(input())) else 'NO')

# set1 = set(int(i) for i in input().split())
# set2 = set(int(i) for i in input().split())
# set3 = set(int(i) for i in input().split())
# print(*sorted((set1 & set2) - set3, reverse=True))

# set1 = set(int(i) for i in input().split())
# set2 = set(int(i) for i in input().split())
# set3 = set(int(i) for i in input().split())
# print(*sorted((set1 | set2 | set3) - (set1 & set3 & set2)))

# set1 = set(int(i) for i in input().split())
# set2 = set(int(i) for i in input().split())
# set3 = set(int(i) for i in input().split())
# print(*sorted(set3 - (set1 | set2), reverse=True))

# set1 = set(int(i) for i in input().split())
# set2 = set(int(i) for i in input().split())
# set3 = set(int(i) for i in input().split())
# my_set = set(range(11))
# print(*sorted(my_set - (set1 | set2 | set3)))

# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
# my_set = {int(c) for c in items}
# print(*sorted(my_set))

# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon',
#          'tangerine', 'Watermelon', 'currant', 'Almond']
# my_set = {c[0].lower() for c in words}
# print(*sorted(my_set))

# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a
# pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if
# you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know
# those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed
# by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# my_set = {word.lower().strip('().,;:-?!') for word in sentence.split()}
# print(*sorted(my_set))

# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a
# pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if
# you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know
# those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed
# by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# my_set = {word.lower().strip('().,;:-?!') for word in sentence.split() if len(word.strip('().,;:-?!')) < 4}
# print(*sorted(my_set))

# files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT',
#          'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py',
#          'stepik.org', 'kotlin.ko', 'github.git']
# my_set = {i.lower() for i in files if i.lower().endswith('.png')}
# print(*sorted(my_set))


# """ Счётчик верных решений ✅🌶️🌶️ """
# correct_set = set()
# wrong = 0
# n = int(input())
# for _ in range(n):
#     name, result = input().split(': ')
#     if result == 'Correct':
#         correct_set.add(name)
#     else:
#         wrong += 1
# if correct_set:
#     count = int(100 - (wrong / n) * 100 + 0.5)
#     print(f'''Верно решили {len(correct_set)} учащихся
# Из всех попыток {count}% верных''')
# else:
#     print('Вы можете стать первым, кто решит эту задачу')
