# 3 Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

# # До 
# import random

# def num_list_generator(list_length, min_value, max_value):
#     result_list =[]
#     for i in range (list_length):
#         result_list.append(random.randint(min_value,max_value))
#     return result_list

# def num_list_uniq (list):
#     result_list = []
#     for i in list:
#         if list.count(i) == 1:
#             result_list.append(i)
#     return result_list

# my_list = num_list_generator(14,0,10)
# print(my_list)
# print(num_list_uniq(my_list))

# После
from random import randint
my_list = [randint(1,10) for x in range(15)]
print(my_list)

def uniq_numbers (list):
    result_list = [x for x in list if list.count(x) == 1]
    return(result_list)
print(uniq_numbers(my_list))