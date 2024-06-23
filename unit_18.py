# """ Количество строк в файле """
# with open(input(), encoding='utf-8') as file:
#     input_lines = [line.strip() for line in file.readlines()]
#     print(len(input_lines))


# """ Суммарная стоимость """
# with open('ledger.txt', encoding='utf-8') as file:
#     lines = [int(line.strip()[1::]) for line in file.readlines()]
#     print(f'${sum(lines)}')


# """ Goooood students """
#
#
# def compare_mark(marks: list):
#     flag = False
#     for mark in marks:
#         if int(mark) > 64:
#             flag = True
#         else:
#             flag = False
#             break
#     return flag
#
#
# with open('grades.txt', encoding='utf-8') as file:
#     lines = [line.strip().split() for line in file.readlines()]
#     count = 0
#     for line in lines:
#         if compare_mark(line[1::]):
#             count += 1
#     print(count)


# """ Самое длинное слово в файле """
# with open('words.txt', encoding='utf-8') as file:
#     data = file.read().split()
#     max_len = 0
#     for i in data:
#         if len(i) > max_len:
#             max_len = len(i)
#     for i in data:
#         if len(i) == max_len:
#             print(i)


# """ Tail of a File """
# with open(input(), encoding='utf-8') as file:
#     lines = [line.strip() for line in file.readlines()]
#     print(*lines[-10:], sep='\n')


# """ Forbidden words 🌶️ """
# with open('forbidden_words.txt', encoding='utf-8') as file:
#     forbidden_words = file.read().split()
#
# with open(input(), encoding='utf-8') as file:
#     line = file.read()
#     double_line = line.lower()
#     for forbidden_word in forbidden_words:
#         if forbidden_word in double_line:
#             double_line = double_line.replace(forbidden_word, len(forbidden_word) * '*')
#     for i in range(len(double_line)):
#         if double_line[i] == '*':
#             print('*', end='')
#         else:
#             print(line[i], end='')


# """ Транслитерация 🌶️ """
# translate_dict = {
#     'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
#     'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
#     'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
#     'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya',
#     'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch',
#     'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*',
#     'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je',
#     'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya',
#     }
#
# with open('cyrillic.txt', encoding='utf-8') as file, open('transliteration.txt', 'a', encoding='utf-8') as output_file:
#     line = file.read()
#     new_line = ''
#     for char in line:
#         if char in translate_dict.keys():
#             char = char.replace(char, translate_dict[char])
#             new_line += char
#         else:
#             new_line += char
#     print(new_line, file=output_file)


# """ Пропущенные комменты 🌶️ """
# with open(input(), encoding='utf-8') as file:
#     lines = [line.strip() for line in file.readlines()]
#     new_lines = []
#     for i in range(len(lines)):
#         if lines[i].startswith('#') and lines[i + 1].startswith('def'):
#             continue
#         elif lines[i][:3] == 'def' and not lines[i - 1].startswith('#'):
#             index = lines[i].index('(')
#             new_lines.append(lines[i][4:index])
#     if len(new_lines) == 0:
#         print('Best Programming Team')
#     else:
#         print(*new_lines, sep='\n')
