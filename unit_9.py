""" Домашнее задание """
# n, m, k, p = [int(input()) for _ in range(4)]
# print(n - m - k + p)

""" Восход """
# lst = list(map(int, input().split()))
# my_set = set(lst)
# print(len(lst) - len(my_set))

""" Города """
# num = int(input())
# lst = []
# for _ in range(num):
#     lst.append(input())
# word = input()
# print('OK' if word not in lst else 'REPEAT')

""" Книги на прочтение """
# n, m = [int(input()) for _ in range(2)]
# my_set = set()
# for _ in range(n):
#     my_set.add(input())
# for _ in range(m):
#     if input() in my_set:
#         print('YES')
#     else:
#         print('NO')

""" Странное увлечение """
# set1 = set(int(i) for i in input().split())
# set2 = set(int(i) for i in input().split())
# if len(set1 & set2) == 0:
#     print('BAD DAY')
# else:
#     print(*sorted(set1 & set2, reverse=True))

""" Онлайн-школа BEEGEEK 1 """
# set1 = set(int(i) for i in input().split())
# set2 = set(int(i) for i in input().split())
# print('YES' if set1 == set2 else 'NO')

""" Онлайн-школа BEEGEEK 2 """
# n, m = [int(input()) for _ in range(2)]
# set1 = set(input() for _ in range(n))
# set2 = set(input() for _ in range(m))
# print(len(set1 - set2))

""" Онлайн-школа BEEGEEK 3 """
# n, m = [int(input()) for _ in range(2)]
# set1 = set(input() for _ in range(n))
# set2 = set(input() for _ in range(m))
# if len(set1 ^ set2) == 0:
#     print('NO')
# else:
#     print(len(set1 ^ set2))

""" Онлайн-школа BEEGEEK 4 """
# lst1 = list(map(str, input().split()))
# lst2 = list(map(str, input().split()))
# print(*sorted(set(lst1) | set(lst2)))

""" Онлайн-школа BEEGEEK 5 """
# n, m = [int(input()) for _ in range(2)]
# lst = [input() for _ in range(n + m)]
# set1 = set(lst)
# for i in lst:
#     if lst.count(i) > 1:
#         set1.discard(i)
# if len(set1) == 0:
#     print('NO')
# else:
#     print(len(set1))

""" Онлайн-школа BEEGEEK 6 """
# m = int(input())
# n = int(input())
# first_set = set([input() for _ in range(n)])
# empty_set = set()
# if m == 1:
#     print(*sorted(first_set), sep='\n')
#     quit()
# for i in range(m - 1):
#     for j in range(int(input())):
#         empty_set.add(input())
#     first_set.intersection_update(empty_set)
#     empty_set.clear()
# print(*sorted(first_set), sep='\n')
