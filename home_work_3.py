# 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.
#
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# some_list = [2, 3, 5, 9, 3]
# new_some_list = []
# sum = 0
# x = len(some_list)
# for i in range(0, x):
#     if (i % 2) != 0:
#         sum += some_list[i]
#         new_some_list.append(some_list[i])
# print(f'на нечётных позициях элементы',new_some_list, 'ответ:', sum)

# 23. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# new_some_list = []
# x = 0
# some_list = [int(i) for i in input('Введите числа через пробел: ').split()]
# if len(some_list) % 2 != 0:
#     for i in range(0, len(some_list) // 2 + 1):
#         x = some_list[i] * some_list[len(some_list) - i - 1]
#         new_some_list.append(x)
# else:
#     for i in range(0, len(some_list) // 2):
#         x = some_list[i] * some_list[len(some_list) - i - 1]
#         new_some_list.append(x)
# print(new_some_list)


# 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
#
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# new_some_list = []
# some_list = [1.1, 1.2, 3.1, 5, 10.01]
# for i in range(0, len(some_list)):
#     if some_list[i] % 1 != 0:
#         new_some_list.append(round(some_list[i] % 1,2))
# print(new_some_list)
# print(max(new_some_list) - min(new_some_list))

# 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# some_list = []
# num = int(input('Введите десятичное число: '))
# while num > 1:
#     x = num % 2
#     num = num // 2
#     some_list.append(x)
# some_list.append(num)
# some_list.reverse()
# print(*some_list, sep='')

# ------------2 вариант-------------------
# num_2 = ""
# num = int(input('Введите десятичное число: '))
# while num != 0:
#     num_2 = str(num % 2) + num_2
#     num //= 2
# print(num_2)


# 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

