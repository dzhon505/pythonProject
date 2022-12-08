# 30. Вычислить число c заданной точностью d
#
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# from math import pi
# d = str(input())
# print(str(pi)[:len(d)])

# 31. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

# num = int(input('Введите натуральное число: '))
# simple_list = []
# for i in range(1, num + 1):
#     if num % i == 0:
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             simple_list.append(i)
# print(simple_list)


# 32. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
some_list = [randint(1, 9) for _ in range(9)]
new_list = []
nums = set()
for i in range(0, 9):
    if some_list[i] not in nums:
        nums.add(some_list[i])
        for j in range(i + 1, 9):
            if some_list[i] == some_list[j]:
                break
        else:
            new_list.append(some_list[i])
print(some_list)
print(new_list)


