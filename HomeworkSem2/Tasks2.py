# 1.Найти сумму чисел списка стоящих на нечетной позиции # Пример:[1,2,3,4] -> 4
# num = [1, 2, 3, 4, 5, 6]
# sum = 0
# for i in range(len(num)):
#     if num[i] % 2 != 0:
#         sum += num[i]
# print(num)
# print(f'Сумма чисел списка стоящих на нечетной позиции = {sum}')


# 2.Найти произведение пар чисел в списке. Парой считаем первый и последний элемент,
#  второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 


# number_list = [2, 3, 5, 6]
# # number_list = [2, 3, 4, 5, 6]
# result_list = []
# prod = 1
# len = len(number_list)
# for i in range(len//2):
#     prod = number_list[i] * number_list[len - i - 1]
#     result_list.append(prod)
# if len % 2 != 0:
#     result_list.append(number_list[len//2]*number_list[len//2])
# print(f'произведение пар чисел в списке = {result_list}')


# 3.В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением 
# дробной части элементов. 

# import math
# from decimal import Decimal
# numbers_list = ['1.1', '1.2', '3.1', '5', '10.01']
# decimal_numbers_list = list(map(Decimal, numbers_list))


# min_fract = decimal_numbers_list[0] - math.floor(decimal_numbers_list[0])
# max_fract = decimal_numbers_list[0] - math.floor(decimal_numbers_list[0])

# for i in range(len(numbers_list)):
#     if decimal_numbers_list[i] - math.floor(decimal_numbers_list[i]) > max_fract:
#         max_fract = decimal_numbers_list[i] - math.floor(decimal_numbers_list[i])
    
#     if decimal_numbers_list[i] - math.floor(decimal_numbers_list[i]) < min_fract:
#         min_fract = decimal_numbers_list[i] - math.floor(decimal_numbers_list[i])

# print(f'Разница между максимальной вещественной частью и минимальной = {max_fract - min_fract}')



# 4.Написать программу преобразования десятичного числа в двоичное

# n = int(input('Введите десятичное число n = '))
# binary_number = ''
# new_n = n
# if new_n == 0:
#     binary_number = binary_number + str(0)
# while new_n > 0:
#     binary_number = str(new_n % 2) + binary_number
#     new_n =new_n //2
# print(f'число {n} в двоичой системе = {binary_number}')


