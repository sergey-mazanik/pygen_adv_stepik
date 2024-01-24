# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
# last = countries[-1]
# print(last)

# primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
# print(primes[:6])

# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain',
# 'Ukraine', 'Chile', 'Cameroon')
# print(countries[2:])

# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain',
# 'Ukraine', 'Chile', 'Cameroon')
# print(countries[:-3])

# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy',
#              'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[3:-2])

# countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
# number = len(countries)
# print(number)

# numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
# print(min(numbers) + max(numbers))

# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
# index = countries.index('Slovenia')
# print(index)

# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy',
#              'Spain', 'Ukraine', 'Chile', 'Spain', 'Cameroon')
# number = countries.count('Spain')
# print(number)

# numbers1 = (1, 2, 3)
# numbers2 = (6,)
# numbers3 = (7, 8, 9, 10, 11, 12, 13)
# print(numbers1 * 2 + numbers2 * 9 + numbers3)

# city_name = input()
# city_year = int(input())
# city = (city_name, city_year)
# print(city)

# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# non_empty_tuples = list(filter(lambda i: len(i) > 0, tuples))
# print(non_empty_tuples)

# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# new_tuples = [tuples[i][:-1] + (100,) for i in range(len(tuples))]
# print(new_tuples)

# poets = [
#     ("Есенин", 13),
#     ("Тургенев", 14),
#     ("Маяковский", 28),
#     ("Лермонтов", 20),
#     ("Фет", 15),
# ]
#
# for i in range(len(poets)):
#     for j in range(i + 1, len(poets)):
#         if poets[i][1] > poets[j][1]:
#             poets[i], poets[j] = poets[j], poets[i]
#
# print(poets[0])
# print(poets[-1])


# poets = [
#     ("Тургенев", 14),
#     ("Есенин", 13),
#     ("Маяковский", 28),
#     ("Фет", 15),
#     ("Лермонтов", 20),
# ]
#
# for i in range(len(poets)):
#     for j in range(i + 1, len(poets)):
#         if poets[i] > poets[j]:
#             poets[i], poets[j] = poets[j], poets[i]
#
# print(poets[0])
# print(poets[-1])


# numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
# multi = 1
# for i in numbers:
#     multi *= i
# print(multi)

# data = 'Python для продвинутых!'
# print(tuple(data))

# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# poet_data_list = list(poet_data)
# poet_data_list[2] = 'Москва'
# poet_data = tuple(poet_data_list)
# print(poet_data)


# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# lst = []
# for i in numbers:
#     lst1 = []
#     for j in i:
#         lst1.append(j)
#     lst.append(sum(lst1) / len(i))
#     lst1.clear()
# print(lst)
