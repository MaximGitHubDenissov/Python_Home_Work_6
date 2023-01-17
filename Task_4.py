# 3 Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

#  ДО

# n = int(input('Введите число n:  '))
# my_list = []
# for i in range(1, n+1):
#     my_list.append((1+1/i)**i)
# print(my_list)
# sum = 0
# for i in my_list:
#     sum = sum+i
# print(round(sum, 2))

# После

my_list = [(1+1/x)**x for x in range (1, int(input('Введите число N: '))+ 1)]
print(my_list)
print(round(sum(my_list),2)) 