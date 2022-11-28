# print('Ввдедите a')
# a = int(input())
# print('Ввдедите b')
# b = int(input())
# if a ** 2 == b or b ** 2 == a:
#     print('yes')
# else:
#     print('no')
#########################################

# some_str = input().split()
# print(some_str)

# numbers = []
# for _ in range(5):
#     n = int(input())
#     numbers.append(n)
# maxx = numbers[0]
# for el in numbers:
#     if el > maxx:
#         maxx = el
# print(maxx)

# maxx = int(input())
# for _ in range(4):
#     n = int(input())
#     if n > maxx:
#         maxx = n
# print(maxx)


# print(max(map(int, input().split())))
#######################################


# a = [1, 9, -1]
# a.append(7)
# print(a)

#######################################
# 3. Напишите программу которая будет на вход принимать число n и выводить числа от -n до n

# list = []
# n = int(input())
# for i in range(-n, n):
# #     list.append(i)
# # print(list)
#     print(i, end=', ')
# print(n)
######################################

# n = int(input())
# print(*list(range(-n, n +1)),sep=', ')

######################################

# n = int(input())
# some_str = ''
# for i in range(-n, n + 1):
#     some_str += str(i) + ', '
# print(some_str[:-2])

# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# some_str = input()
# if ',' in some_str:
#     some_list = some_str.split(',')
#     print(some_list[1][0])
# else:
#     print('NO')
#####################

# some_str = input()
# if ',' in some_str:
#     ind = some_str.index(',')
#     print(some_str[ind + 1])
# else:
#     print('NO')

#####################

# number = float(input())
# number = number * 10
# number = int(number)
# print((number % 10))

############################################

# 5. Напишите программу, которая принимает на вход число и проверяет, кратно
# ли оно 5 и 10 или 15, но не 30.

n = int(input())
if (n % 5 == 0 and n % 10 == 0 or n % 15 == 0) and n % 30 != 0:
    print('YES')
else:
    print('NO')