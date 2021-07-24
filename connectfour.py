"""
Connect four program written by Thor.N from scratch
Started on 7/24/2021 at 00:31
"""
import os

#initial settings for cleaner game and terminal
clear = lambda: os.system('cls')
pause = lambda: input('\nPlease press Enter to continue...')

"""
print(' --- --- --- --- --- --- --- ')
print(' | ' + playing_board[0][0] + ' | ' + playing_board[0][1] + ' | ' + playing_board[0][2] + ' | ' playing_board[0][3] + ' | ' + playing_board[0][4] + ' | ' + playing_board[0][5] + ' | ' playing_board[0][6] + ' |')
print(' --- --- --- --- --- --- --- ')
print(' | ' + playing_board[1][0] + ' | ' + playing_board[1][1] + ' | ' + playing_board[1][2] + ' | ' playing_board[1][3] + ' | ' + playing_board[1][4] + ' | ' + playing_board[1][5] + ' | ' playing_board[1][6] + ' |')
print(' --- --- --- --- --- --- --- ')
print(' | ' + playing_board[2][0] + ' | ' + playing_board[2][1] + ' | ' + playing_board[2][2] + ' | ' playing_board[2][3] + ' | ' + playing_board[2][4] + ' | ' + playing_board[2][5] + ' | ' playing_board[2][6] + ' |')
print(' --- --- --- --- --- --- --- ')
print(' | ' + playing_board[3][0] + ' | ' + playing_board[3][1] + ' | ' + playing_board[3][2] + ' | ' playing_board[3][3] + ' | ' + playing_board[3][4] + ' | ' + playing_board[3][5] + ' | ' playing_board[3][6] + ' |')
print(' --- --- --- --- --- --- --- ')
print(' | ' + playing_board[4][0] + ' | ' + playing_board[4][1] + ' | ' + playing_board[4][2] + ' | ' playing_board[4][3] + ' | ' + playing_board[4][4] + ' | ' + playing_board[4][5] + ' | ' playing_board[4][6] + ' |')
print(' --- --- --- --- --- --- --- ')
print(' | ' + playing_board[5][0] + ' | ' + playing_board[5][1] + ' | ' + playing_board[5][2] + ' | ' playing_board[5][3] + ' | ' + playing_board[5][4] + ' | ' + playing_board[5][5] + ' | ' playing_board[5][6] + ' |')
print(' --- --- --- --- --- --- ---')

"""








def check_for_winner(board):
    pass



def connect4():

    #board that holds the game data
    playing_board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ',],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ',],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ',],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ',],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ',],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ',],
    ]


    clear()
    print('\nWelcome to a python connect4 game writting in the terminal!!')
    print('The first player will be RED, the other player is YELLOW')
    pause()
    clear()

    winner = False
    turn = 'RED'
    while (winner == False):

        #displays who is currently playing
        if (turn == 'RED'):
            print(' ___  ___  ___ ')
            print('| _ \| __||   \ ')
            print('|   /| _| | |) |')
            print('|_|_\|___||___/')
        elif (turn == 'YELLOW'):
            print('__   __ ___  _     _      ___  __      __')
            print('\ \ / /| __|| |   | |    / _ \ \ \    / /')
            print(' \   / | _| | |__ | |__ | (_) | \ \/\/ / ')
            print('  |_|  |___||____||____| \___/   \_/\_/  ')
        print(' ')


        #prints out current board
        print(' --- --- --- --- --- --- --- ')
        print('| ' + playing_board[0][0] + ' | ' + playing_board[0][1] + ' | ' + playing_board[0][2] + ' | ' + playing_board[0][3] + ' | ' + playing_board[0][4] + ' | ' + playing_board[0][5] + ' | ' + playing_board[0][6] + ' |')
        print(' --- --- --- --- --- --- --- ')
        print('| ' + playing_board[1][0] + ' | ' + playing_board[1][1] + ' | ' + playing_board[1][2] + ' | ' + playing_board[1][3] + ' | ' + playing_board[1][4] + ' | ' + playing_board[1][5] + ' | ' + playing_board[1][6] + ' |')
        print(' --- --- --- --- --- --- --- ')
        print('| ' + playing_board[2][0] + ' | ' + playing_board[2][1] + ' | ' + playing_board[2][2] + ' | ' + playing_board[2][3] + ' | ' + playing_board[2][4] + ' | ' + playing_board[2][5] + ' | ' + playing_board[2][6] + ' |')
        print(' --- --- --- --- --- --- --- ')
        print('| ' + playing_board[3][0] + ' | ' + playing_board[3][1] + ' | ' + playing_board[3][2] + ' | ' + playing_board[3][3] + ' | ' + playing_board[3][4] + ' | ' + playing_board[3][5] + ' | ' + playing_board[3][6] + ' |')
        print(' --- --- --- --- --- --- --- ')
        print('| ' + playing_board[4][0] + ' | ' + playing_board[4][1] + ' | ' + playing_board[4][2] + ' | ' + playing_board[4][3] + ' | ' + playing_board[4][4] + ' | ' + playing_board[4][5] + ' | ' + playing_board[4][6] + ' |')
        print(' --- --- --- --- --- --- --- ')
        print('| ' + playing_board[5][0] + ' | ' + playing_board[5][1] + ' | ' + playing_board[5][2] + ' | ' + playing_board[5][3] + ' | ' + playing_board[5][4] + ' | ' + playing_board[5][5] + ' | ' + playing_board[5][6] + ' |')
        print(' --- --- --- --- --- --- ---')
        
        pause()



        if (turn == 'RED'):
            turn = 'YELLOW'
        elif (turn == 'YELLOW'):
            turn = 'RED'

connect4()
pause()