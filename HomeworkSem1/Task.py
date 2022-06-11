# 1 Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

# N = int(input('Введите количество членов последовательности N = '))
# result_list = []
# for i in range(0, N):
#     result_list.append((-3)**i)
# print(f'Для N = {N} список = {result_list}')


# 2 Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

# n = int(input('Введите количество элементов словаря:  '))
# dictionary = {}
# for i in range(1, n + 1):
#     dictionary[i] = 3*i + 1
# print(f'Для n = {n} словарь значений = {dictionary}')


# 3 ользователь задаёт две строки. Определить количество вхождений одной строки в другой.

# string1 = input("Введите строку 1: ")
# string2 = input("Введите строку 2: ")
#
# if len(string1) >= len(string2):
#     part_string = string1.split(string2)
#     print(f'Количество вхождений строки 2 в строку 1 = {len(string1.split(string2)) - 1}')
# else:
#     part_string = string2.split(string1)
#     print(f'Количество вхождений строки 1 в строку 2 = {len(string2.split(string1)) - 1}')


# 4 Подсчитать сумму цифр в вещественном числе.

# Вариант 1

# number = input('Введите вещественное число: ')
# sum = 0
# for i in number:
#     if i != '-' and i != '.' and i != ',':
#         sum += int(i)
# print(sum)

# Вариант 2

# number = float(input('Введите вещественное число: '))
# # num = -123.124
# a = number
# if a < 0:
#     a *= -1
# sum = 0
# for i in str(a):
#     a = a * 10
# while (a > 0):
#     sum = sum + a % 10
#     a = a // 10
# print(f'сумма цифр в вещественном числе {number} = {int(sum)}')


# 5 Написать программу получающую набор произведений чисел от 1 до N. Пример: пусть N = 4, 
# тогда [ 1, 2, 6, 24 ]


# N = int(input('Введите число N ='))
# result_list = []
# product = 1
# for i in range(1,N+1):
#     product *= i
#     result_list.append(product)
# print(f'набор произведений чисел от 1 до {N} = {result_list}')