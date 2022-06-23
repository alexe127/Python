# 1.Дан список чисел. Создать список, в который попадают числа, 
# описываемые возрастающую последовательность.
#  Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. 
# Порядок элементов менять нельзя

# def ascending_sequence(nums):
#     result_list = []
#     for i in range(len(nums)):
#         if i == 0:
#             result_list.append(nums[i])
#         elif nums[i] > result_list[len(result_list) - 1]:
#             result_list.append(nums[i])
#     return result_list


# nums_list = [0, 1, 0, 5, 2, 3, 4, 6, 1, 7]
# print(nums_list)
# print(f'Возрастающая последовательность =  {ascending_sequence(nums_list)}')


# 2.Создать и заполнить файл случайными целыми значениями. 
# Выполнить сортировку содержимого файла по возрастанию. 

# import random

# def random_number(quantity, file_name):
#     with open(file_name, 'w') as data:
#         for i in range(quantity):
#             new_data = str(random.randint(0, 100)) + "\n"
#             data.write(new_data)
            
# def print_file(file_name):
#     with open(file_name, 'r') as data:
#         for line in data:
#             print(line, end= '')
    

# def sort_number_in_file(file_name):
#     with open(file_name, 'r') as data:
#         data_from_file = data.readlines()
#         list_from_file = list(map(int, data_from_file))
        
#     list_from_file.sort()
#     print(f'отсортированный список в файле {list_from_file} ')

#     with open(file_name, 'w') as data:
#         for i in list_from_file:
#             data.write(f'{i} ')    


# file = 'file_s4-t2.txt'

# random_number(6, file)
# print(f'случайные числа в файле:')
# print_file(file)
# sort_number_in_file(file)


# 3.	Вот вам файл с тысячей чисел. 1Kints.txt
# Задача: найти триплеты и просто выводить их на экран. Триплетом называются три числа, 
# которые в сумме дают 0.


# def read_numbers_from_file(file):
#     with open(file, 'r') as data:
#         number_from_file = data.readlines()
#         list_result = list(map(int, number_from_file))
#     return list_result

# def find_triplet(nums_list):
#     count = 0
#     for i in range(len(list_result)-2):
#         for j in range(i+1, len(list_result)-1):
#             for k in range(j+1, len(list_result)):
#                 if(list_result[i] + list_result[j] + list_result[k] == 0):
#                     print(f'{list_result[i]} + {list_result[j]} + {list_result[k]} = 0')
#                     count += 1
#     print(f'Количество триплетов равно {count}')

# file = '1Kints.txt'
# list_result = read_numbers_from_file(file)
# find_triplet(list_result)