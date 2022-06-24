###Написать программу вычисления арифметического выражения заданного строкой. 
##Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
##Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# 

# OPERATORS = {
#     '+': (1, lambda x, y: x + y),
#     '-': (1, lambda x, y: x - y),
#     '*': (2, lambda x, y: x * y),
#     '/': (2, lambda x, y: x / y)
# }

# def calc(polish):
#     stack = []
#     for token in polish:
#         if token in OPERATORS:  
#             y, x = stack.pop(), stack.pop()  
#             stack.append(OPERATORS[token][1](x, y)) 
#         else:
#             stack.append(token)
#     return stack[0] 

# def sort_polish(infix):
#     postfix = []
#     stack = []
#     for token in infix:
#         if token in OPERATORS:
#             while stack and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
#                 postfix.append(stack.pop())
#             stack.append(token)
#         else:
#             postfix.append(token)
#     while stack:
#         postfix.append(stack.pop())
#     return postfix


# def parse_infix(math_expression):
#     polish = []
#     number = ''
#     for s in math_expression:
#         if s.isdigit(): 
#             number += s
#         else: 
#             polish.append(float(number))
#             number = ''
#         if s in OPERATORS: 
#             polish.append(s)
#     if number:  
#         polish.append(float(number))
#     return polish


# def calc_math_expression(math_expression):
#     polish_infix = parse_infix(math_expression)
#     polish = sort_polish(polish_infix)
#     return calc(polish)

# math_expression = '2+3*2-4*3'
# res = calc_math_expression(math_expression)
# print(res)



## 2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. 
## Входные и выходные данные хранятся в отдельных файлах 
## (в одном файлике отрывок из какой-то книги, а во втором файлике — сжатая версия этого текста). 


# def rle_encode(data):
#     encoded = []
#     count = 1
#     for i in range(len(data)):
#         if i == len(data) - 1: 
#             encoded.append(str(count))
#             encoded.append(data[i])
#         elif data[i] == data[i + 1]: 
#             count += 1
#         else: 
#             encoded.append(str(count))
#             encoded.append(data[i])
#             count = 1
#     return ''.join(encoded)

# def rle_decode(data):
#     decoded = []
#     number = 0
#     for i in range(len(data)):
#         if data[i].isdigit():
#             number = number * 10 + int(data[i])
#         else:
#             decoded.append(data[i] * number)
#             number = 0
#     return ''.join(decoded)

# def read_text_from_file(file_name):
#     file = open(file_name, 'r', encoding='UTF-8')
#     data = file.read()
#     file.close()
#     return data

# def write_text_in_file(file_name, text):
#     file = open(file_name, 'w', encoding='UTF-8')
#     file.write(text)
#     file.close()
 
# text = read_text_from_file('text.txt')

# encode_text = rle_encode(text)
# write_text_in_file('encode_text.txt', encode_text)
# decode_text = rle_decode(encode_text)
# write_text_in_file('decode_text.txt', decode_text)

## 3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв
##  после нее в алфавите. ROT13 является примером шифра Цезаря.
## Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 .
##  Если в строку включены числа или специальные символы, они должны быть возвращены как есть. 
## Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений). 
## Не использовать функцию encode.

# def code_Rot13(text):
#     result = ''
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     for char in text:
#         digital = alphabet.find(char.lower())        
#         if digital != -1:
#             char = alphabet[(digital + 13) % len(alphabet)]
#         else:
#             char = char
#         result += char
#     return result

# text = ' qwertY ASdfgh =997y / , zxc '

# print(f'Закодированный текст: {code_Rot13(text)}')                   
# print(f'Декодированный текст: {code_Rot13(code_Rot13(text))}')     