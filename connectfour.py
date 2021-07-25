"""
Connect four program written by Thor.N from scratch
Started on 7/24/2021 at 00:31
"""

import os

#initial settings for cleaner game and terminal
clear = lambda: os.system('cls')
pause = lambda: input('\nPlease press Enter to continue...')









def check_winner(board):
    board_reversed = board[::-1] #reverses the board so it can scan and check from bottom to top
    

    def check_rows(input_board): 
        for row in input_board:
            
            for slot in range(len(row)):
                if (slot >= 4):
                    continue
                else:
                    if (row[slot] == 'R') and (len(set(row[slot:slot+4])) == 1):
                        return 'R'
                    elif (row[slot] == 'Y') and (len(set(row[slot:slot+4])) == 1):
                        return 'Y'
                
        
    def check_collumns():

        transposed_board = [[row[i] for row in board_reversed] for i in range(len(board_reversed[0]))]

        #uses check_rows because if functions the same way when the board transposed
        return check_rows(transposed_board)

        #manual version instead of using check_rows
        """for row in transposed_board:
            
            print(row)
            for slot in range(len(row)):
                if (slot >= 4):
                    
                    continue
                else:
                    if (row[slot] == 'R') and (len(set(row[slot:slot+4])) == 1):
                        print(row[slot:slot+4])
                        return 'R'
                    elif (row[slot] == 'Y') and (len(set(row[slot:slot+4])) == 1):
                        return 'Y'"""

        
    
    #returns who the winner is
    if (' ' in board[0]):
        if (check_rows(board_reversed) == 'R') or (check_collumns() == 'R'):
            return 'R'
        elif (check_rows(board_reversed) == 'Y') or (check_collumns() == 'Y'):
            return 'Y'
    else:
        return 'draw'





def connect4():

    

    #board that holds the game data
    playing_board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ',],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ',],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ',],
        ['Y', ' ', ' ', ' ', ' ', ' ', 'R',],
        ['Y', ' ', ' ', ' ', ' ', ' ', 'R',],
        ['Y', 'Y', 'Y', ' ', ' ', ' ', 'R',],
    ]


    clear()
    print('\nWelcome to a python connect4 game writting in the terminal!!')
    print('The first player will be RED, the other player is YELLOW')
    pause()
    clear()

    winner = ''
    turn = 'R'
    while (winner == ''):
        
        #checks for a winner
        if (check_winner(playing_board) == 'R') or (check_winner(playing_board) == 'Y') or (check_winner(playing_board) == 'draw'):
            winner = check_winner(playing_board)
            break



        #displays who is currently playing
        if (turn == 'R'):
            print(' ___  ___  ___ ')
            print('| _ \| __||   \ ')
            print('|   /| _| | |) |')
            print('|_|_\|___||___/')
        elif (turn == 'Y'):
            print('__   __ ___  _     _      ___  __      __')
            print('\ \ / /| __|| |   | |    / _ \ \ \    / /')
            print(' \   / | _| | |__ | |__ | (_) | \ \/\/ / ')
            print('  |_|  |___||____||____| \___/   \_/\_/  ')
        print(' ')


        #prints out current board
        print('  1 - 2 - 3 - 4 - 5 - 6 - 7')
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
        

        #prompts user for a slot
        chosen_slot = input('Pick a slot number to drop your token: ')
        slots = '1234567'

        
        clear()

        
        #starts process of placing the token
        if (chosen_slot in slots) and (chosen_slot):
            chosen_slot = int(chosen_slot)
            chosen_slot -= 1

            #places token in chosen row
            for row in range(len(playing_board)):
                if (playing_board[::-1][row][chosen_slot] == ' '):
                    playing_board[::-1][row][chosen_slot] = turn
                    break
                    
        #makes sure valid slots are entered into chosen_slot
        else:       
            print('Sorry that is not a valid game slot number.')
            input('\nPress Enter to try again...')
            continue
        

        #switches turn if there is no winner
        if (winner == ''):
            
            if (turn == 'R'):
                turn = 'Y'
            elif (turn == 'Y'):
                turn = 'R'

    #prints the winner message
    print(' ')
    if (winner == 'R'):
        #print('Congrats, the winner of the game is RED!!!')
        print(' ___  ___  ___        __      __ ___  _  _  ___  ')
        print('| _ \| __||   \       \ \    / /|_ _|| \| |/ __| ')
        print('|   /| _| | |) |       \ \/\/ /  | | | .  |\__ \ ')
        print('|_|_\|___||___/         \_/\_/  |___||_|\_||___/ ')
    elif(winner == 'Y'):
        #print('Congrats, the winner of the game is YELLOW!!!')
        print('__   __ ___  _     _      ___  __      __      __      __ ___  _  _  ___  ')
        print('\ \ / /| __|| |   | |    / _ \ \ \    / /      \ \    / /|_ _|| \| |/ __| ')
        print(' \   / | _| | |__ | |__ | (_) | \ \/\/ /        \ \/\/ /  | | | .  |\__ \ ')
        print('  |_|  |___||____||____| \___/   \_/\_/          \_/\_/  |___||_|\_||___/ ')
    elif (winner == 'draw'):
        #print('It\'s a draw!!!')
        print(' ___    ___   ___  __      __  _  ') 
        print('|   \  | _ \ /   \ \ \    / / | | ') 
        print('| |) | |   / | - |  \ \/\/ /  |_| ') 
        print('|___/  |_|_\ |_|_|   \_/\_/   (_) ') 



connect4()
pause()