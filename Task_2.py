# Напишите программу, которая принимает на вход вещественное 
# число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11
# До
# my_num = input ('Введите число ')
# sum = 0
# for i in my_num:
#     if i.isdigit():
#         sum += int(i)
# print (sum)
# После
def float_digits_sum (num):
    total = 0
    for elm in num:
        if elm.isdigit():
            total += int(elm)
    return(total)

print(float_digits_sum(input('Введите вещественное число: ')))