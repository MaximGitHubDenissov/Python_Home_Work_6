# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# # ДО
# my_list = [2, 3, 5, 9, 3]
# sum = 0
# for i in range(len(my_list)):
#     if i % 2 != 0:
#         sum += my_list[i]
# print(sum)

#После

from random import randint
def sum_odd_positions(list):
    total = 0
    for i in range(len(list)):
        if i%2:
            total += list[i]
    return total
my_list = [randint(1,20) for x in range(9,15)]
print(my_list)
print(sum_odd_positions(my_list))