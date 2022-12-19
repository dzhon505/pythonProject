# Напишите программу, удаляющую из текста все слова, содержащие "абв".

# my_text = 'фбв аблдвд абвлв шгшщгщш'
#
# my_text_list = list(filter(lambda i: 'а' not in i and 'б' not in i and 'в' not in i, my_text.split()))
# print(my_text_list)


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и востановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах

# def press(file, result):
#     with open(file, 'r', encoding='utf-8') as text:
#         with open(result, 'w', encoding='utf-8') as res:
#             inp_str = text.readline()
#             ind = 0
#             out_str = ''
#             count = 1
#             while ind < len(inp_str) - 1:
#                 if inp_str[ind] == inp_str[ind + 1]:
#                     count += 1
#                 else:
#                     if count == 1:
#                         res.write(inp_str[ind])
#                     else:
#                         res.write(str(count) + inp_str[ind])
#                     count = 1
#                 ind += 1
#
#
# press('file.txt', 'result.txt')
#
# def depress(file, result):
#     with open(file, 'r', encoding='utf-8') as text:
#         with open(result, 'w', encoding='utf-8') as res:
#             inp_str = text.readline()
#             count = ''
#             for letter in inp_str:
#                 if letter.isdigit():
#                     count += letter
#                 else:
#                     if count != '':
#                         res.write(int(count) * letter)
#                     else:
#                         res.write(letter)
#                     count = ''
#
#
# depress('result.txt', 'result2.txt')

# Создайте программу для игры в ""Крестики-нолики"".

board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]

victory = [[0, 1, 2],
           [3, 4, 5],
           [6, 7, 9],
           [0, 3, 6],
           [1, 4, 7],
           [2, 5, 8],
           [0, 4, 8],
           [2, 4, 6]]

def print_board():
    print(board[0], end=' ')
    print(board[1], end=' ')
    print(board[2])
    print(board[3], end=' ')
    print(board[4], end=' ')
    print(board[5])
    print(board[6], end=' ')
    print(board[7], end=' ')
    print(board[8])



def game_step(step, symbol):
    ind = board.index(step)
    board[ind] = symbol


def result():
    win = ""

    for i in victory:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
            win = "X"
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O":
            win = "O"
    return win


game_over = False
player_x = True

while game_over == False:

    print_board()

    if player_x == True:
        symbol = "X"
        step = int(input("Игрок Х: "))
    else:
        symbol = "O"
        step = int(input("Игрок 0: "))

    game_step(step, symbol)
    win = result()
    if win != "":
        game_over = True
    else:
        game_over = False
    player_x = not (player_x)
print_board()

print("Победил игрока", win)



