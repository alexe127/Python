import math

# 1.Найти НОК двух чисел

# def find_gcd(num1, num2):
#     if(num1 < num2):
#         num1, num2 = num2, num1
#     while(num2 != 0):
#         remainder = num1 % num2
#         num1, num2 = num2, remainder
#     return num1

# def find_lcm(num1, num2):    
#     return (num1*num2) // find_gcd(num1, num2)

# number1 = int(input('Введите первое целое число:  '))
# number2 = int(input('Введите второе целое число:  '))
# print(f'Нок чисел {number1} и {number2} = {find_lcm(number1, number2)}')

##  для проверки

# print(f'Нок чисел {number1} и {number2} = {(number1 * number2) // math.gcd(number1, number2)} (вариант 2)')

## можно ещё проще 

# print(f'Нок чисел {number1} и {number2} = {math.lcm(number1, number2)} (вариант 3)')


# 2.Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141. 


# def precision_of_pi(num):
#     i = 0
#     while num % 10 != 1:
#         num *= 10
#         i+=1
#     return i


# d = float(input('Введите точность числа Пи(в формате 0.001) = '))

# pi_gauss = 48*math.atan(1/18)+32*math.atan(1/57)-20*math.atan(1/239)

# print(f'число ПИ = {pi_gauss}')
# print(f'нужная точность числа ПИ = {precision_of_pi(d)}')
# pi_gauss1, pi_gauss2 = str(pi_gauss).split('.')
# print(f'число Пи = {pi_gauss1}.{pi_gauss2[:precision_of_pi(d)]}')



# 3.Составить список простых множителей натурального числа N

# def prime_factors_of_number(n):
#     divider = 2
#     multipliers_list = []
#     while(divider <= n):
#         while(n % divider == 0):
#             multipliers_list.append(divider)
#             n //= divider
#         divider += 1
#     return multipliers_list

# N = int(input('Введите число N = '))
# print(f'Список простых множителей числа {N} = {prime_factors_of_number(N)}')




# 4.Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

# def remove_duplicate_elements(list): # просто удаляем повторы
#     new_list =[]
#     for i  in list:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list

# def sort_list(list): # если нужен отсортированный список    
#     length = len(list)    
#     for i in range(length):
#         for j in range(length-i-1):
#             if list[j] > list[j+1]:
#                 list[j], list[j+1]=list[j+1], list[j] 
    
#     # list.sort() # можно использовать вместо цикла for
#     return list

# list = [10, 2, 3, 5, 1, 5, 3, 10]
# print(list)

# print(remove_duplicate_elements(list)) # не меняет порядок списка
# print(sort_list(remove_duplicate_elements(list)))# если нужен отсортированный список

# Вариант 2
# ##### Можно через встроенные функции
# list = [1, 2, 3, 5, 1, 5, 3, 10]
# print(list(set(list))) # удаляет и сортирует список по порядку

# from collections import OrderedDict
# a = [1, 4, 3, 5, 1, 5, 3, 4, 10]
# b = list(OrderedDict.fromkeys(a))  #не меняет порядок списка
# print(b)

# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 

import random

list_of_numbers = []
with open('file.txt', 'w') as data:
    for i in range(random.randint(3,10)):
        rand_num = random.randint(10,100) 
        data.write(f"{rand_num}\n")
        print(rand_num, end= ' ')
with open('file.txt', 'r') as data:
    for line in data:
        line.replace('\n','')
        if int(line) % 2 != 0:
            list_of_numbers.append(line)
with open('file.txt', 'w') as data:
    for i in range(len(list_of_numbers)):
        data.write(list_of_numbers[i])
