# def matrix(n=1, m=None, value=0):
#     if m is None:
#         m = n
#     mat = [[value] * m for _ in range(n)]
#     return mat


# def count_args(*args):
#     return len(args)


# def sq_sum(*args):
#     return sum(i ** 2 for i in args)


# def mean(*args):
#     lst = [i for i in args if type(i) in (int, float)]
#     if len(lst) > 0:
#         return sum(lst) / len(lst)
#     else:
#         return 0.0


# def greet(name, *args):
#     if args:
#         return f'Hello, {name} and {" and ".join(args)}!'
#     else:
#         return f'Hello, {name}!'


# def print_products(*args):
#     products = []
#     for i in args:
#         if isinstance(i, str) and i != '':
#             products.append(i)
#     if products:
#         for i in range(len(products)):
#             print(f'{i + 1}) {products[i]}')
#     else:
#         print('Нет продуктов')


# def info_kwargs(**kwargs):
#     for k, v in sorted(kwargs.items()):
#         print(f'{k}: {v}')
