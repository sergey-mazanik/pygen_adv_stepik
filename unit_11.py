# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21],
#            'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42],
#            'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
# my_dict = {key: [value for value in value if value < 20] for key, value in my_dict.items()}
# print(my_dict)


# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
# result = []
#
# for key, values in emails.items():
#     for value in values:
#         result.append(value + '@' + key)
# print(*sorted(result), sep='\n')


""" Минутка генетики """

# table = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
# dnk = input()
# rnk = ''
# for i in dnk:
#     rnk += table[i]
# print(rnk)


""" Порядковый номер """

# lst = []
# for i in input().split():
#     if i not in lst:
#         print(1, end=' ')
#     else:
#         print(f'{lst.count(i) + 1}', end=' ')
#     lst.append(i)


""" Scrabble game """

# d = {
#     1: "AEILNORSTU",
#     2: "DG",
#     3: "BCMP",
#     4: "FHVWY",
#     5: "K",
#     8: "JX",
#     10: "QZ"
# }
# count = 0
# for i in input():
#     for key, value in d.items():
#         if i in value:
#             count += key
# print(count)


""" Строка запроса """


# def build_query_string(params: dict) -> str:
#     result_list = []
#     for key, value in params.items():
#         result_list.append(f'{key}={value}')
#     result_string = '&'.join(sorted(result_list))
#     return result_string
#
#
# print(build_query_string({'name': 'timur', 'age': 28}))
# print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))


""" Слияние словарей 🌶️ """


# def merge(values: list) -> dict:      # values - это список словарей
#     result_dict = {}
#     for value in values:
#         for k, v in value.items():
#             result_dict.setdefault(k, set()).add(v)
#     return result_dict
#
#
# result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
# print(result)


""" Опасный вирус 😈 """

# permissions = {'write': 'W', 'read': 'R', 'execute': 'X'}
# files_with_permissions = {}
# for i in range(int(input())):
#     file_name, *perm = input().split()
#     files_with_permissions[file_name] = perm
#
# for i in range(int(input())):
#     access, file = input().split()
#     if permissions[access] in files_with_permissions[file]:
#         print('OK')
#     else:
#         print('Access denied')


""" Покупки в интернет-магазине 🌶️ """

# data = {}
# for i in range(int(input())):
#     name, product, count = input().split()
#     data.setdefault(name, {})
#     data[name][product] = data[name].get(product, 0) + int(count)
#
# for k, v in sorted(data.items()):
#     print(f'{k}:')
#     for k1, v1 in sorted(v.items()):
#         print(f'{k1} {v1}')
