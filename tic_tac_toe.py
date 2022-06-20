import random
import time

random.seed(random.randint(1, 1000))

def menu():
    print('Меню:')
    print('1. Новая игра')
    print('2. Играть с компьютером')
    print('3. Справка')
    print('4. Просмотреть результаты')
    print('5. Выход')


def move(board):
    tries = 0
    while True:
        if tries >= 2:
            print('Мда...' * (tries - 1))
        m = input('Выберете клеточку: ')
        if not m.isdigit():
            print('Введите номер клетки')
            tries += 1
            continue
        m = int(m)
        if not 1 <= m <= 9:
            print('Введите номер клетки от 1 до 9.')
            tries += 1
            continue
        m -= 1
        if board[m] != ' ':
            print('Эта клетка занята')
            tries += 1
            continue
        return m


def board_show(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('-----------')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('-----------')
    print(f' {board[6]} | {board[7]} | {board[8]} ')


def winning(board):
    if board[0] == board[1] == board[2] != ' ' or \
            board[3] == board[4] == board[5] != ' ' or \
            board[6] == board[7] == board[8] != ' ' or \
            board[0] == board[4] == board[8] != ' ' or \
            board[6] == board[4] == board[2] != ' ' or \
            board[0] == board[3] == board[6] != ' ' or \
            board[1] == board[4] == board[7] != ' ' or \
            board[2] == board[5] == board[8] != ' ':
        return 'W'
    if ' ' not in board:
        return 'T'
    return 'N'


def reference():
    print()
    print('Справка')
    print('Для хода введите число от 1 до 9')
    print('1 | 2 | 3')
    print('---------')
    print('4 | 5 | 6')
    print('---------')
    print('7 | 8 | 9')
    print('Вам необходимо составить 3 крестика (нолика) в ряд, чтобы победить')
    print('Случайным образом определяется, кто будет ходить за Х, а кто за O')
    print()


def results():
    with open('results.txt', 'r') as file:
        for i in file:
            print(i.strip())


def computer(board, XO):
    for i in range(9):
        if board[i] == ' ':
            board[i] = XO
            if winning(board) == 'W':
                return i
            else:
                board[i] = ' '
    if XO == 'X':
        OX = 'O'
    else:
        OX = 'X'
    for i in range(9):
        if board[i] == ' ':
            board[i] = OX
            if winning(board) == 'W':
                return i
            else:
                board[i] = ' '
    if board[4] == ' ':
        return 4
    corners = [0, 2, 6, 8]
    random.shuffle(corners)
    for i in corners:
        if board[i] == ' ':
            return i
    sides = [1, 3, 5, 7]
    random.shuffle(sides)
    for i in sides:
        if board[i] == ' ':
            return i


def comp_game():
    print('Введите имя: ')
    first = input('Игрок 1: ')
    second = 'Компьютер'
    print('Распределяем крестики и нолики...')
    r = random.randint(0, 1)
    players = {}
    if r == 0:
        players['X'] = first
        players['O'] = second
    else:
        players['X'] = second
        players['O'] = first
    print('X -', players['X'])
    print('O -', players['O'])
    board = [' '] * 9
    turn = 'X'
    board_show(board)
    while True:
        print(f'Ход {turn} - {players[turn]}')
        if players[turn] == second:
            time.sleep(0.5)
            board[computer(board, turn)] = turn
        else:
            board[move(board)] = turn
        board_show(board)
        if winning(board) == 'W':
            print(f'{players[turn]} победил!')
            with open('results.txt', 'a') as file:
                if turn == 'X':
                    print(players['X'], '-', players['O'], '1:0', file=file)
                else:
                    print(players['X'], '-', players['O'], '0:1', file=file)
            break
        elif winning(board) == 'T':
            print('Ничья!')
            with open('results.txt', 'a') as file:
                print(players['X'], '-', players['O'], '1:1', file=file)
            break
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

def new_game():
    print('Введите имена игроков: ')
    first = input('Игрок 1: ')
    second = input('Игрок 2: ')
    print('Распределяем крестики и нолики...')
    r = random.randint(0, 1)
    players = {}
    if r == 0:
        players['X'] = first
        players['O'] = second
    else:
        players['X'] = second
        players['O'] = first
    print('X -', players['X'])
    print('O -', players['O'])
    board = [' '] * 9
    turn = 'X'
    board_show(board)
    while True:
        print(f'Ход {turn} - {players[turn]}')
        board[move(board)] = turn
        board_show(board)
        if winning(board) == 'W':
            print(f'{players[turn]} победил!')
            with open('results.txt', 'a') as file:
                if turn == 'X':
                    print(players['X'], '-', players['O'], '1:0', file = file)
                else:
                    print(players['X'], '-', players['O'], '0:1', file=file)
            break
        elif winning(board) == 'T':
            print('Ничья!')
            with open('results.txt', 'a') as file:
                print(players['X'], '-', players['O'], '1:1', file=file)
            break
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


def game():
    while True:
        menu()
        a = input('Выберите пункт меню: ')
        if a == '1':
            new_game()
        elif a == '2':
            comp_game()
        elif a == '3':
            reference()
        elif a == '4':
            results()
        elif a == '5':
            break
        else:
            print(':|')


game()
