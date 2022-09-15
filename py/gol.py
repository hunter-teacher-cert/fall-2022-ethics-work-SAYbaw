# gol.py
# Steve Sabaugh
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 

import random


def create_new_board(size):
    board = []
    for i in range(size):
        board.append(['-' for j in range(size)])

    for row in range(size):
        for col in range(size):
            if random.random() <= .5:
                board[row][col] = 'X'

    return board


def print_board(board):
    for row in board:
        for each in row:
            print(each, end='  ')
        print()


def count_neighbors(board, r, c):
    livingCt = 0

    for row in range(max(0, r - 1), min(r + 2, len(board))):
        for col in range(max(0, c - 1), min(c + 2, len(board[row]))):
            if not (row == r and col == c):
                if board[row][col] == 'X':
                    livingCt += 1
    return livingCt


def get_next_gen_cell(board, r, c):
    living = count_neighbors(board, r, c)
    if board[r][c] == '-':
        if living == 3:
            return 'X'
        else:
            return '-'
    else:
        if living == 2 or living == 3:
            return 'X'
        else:
            return '-'


def generate_next_board(board):
    newBoard = []
    for i in range(len(board)):
        newBoard.append(['-' for j in range(len(board[0]))])
    for row in range(len(newBoard)):
        for col in range(len(newBoard[row])):
            newBoard[row][col] = get_next_gen_cell(board, row, col)

    return newBoard


gen0 = create_new_board(5)
print_board(gen0)
print()
gen1 = generate_next_board(gen0)
print_board(gen1)
print()
gen2 = generate_next_board(gen1)
print_board(gen2)
print()
gen3 = generate_next_board(gen2)
print_board(gen3)
print()
gen4 = generate_next_board(gen3)
print_board(gen4)
print()
gen5 = generate_next_board(gen4)
print_board(gen5)
