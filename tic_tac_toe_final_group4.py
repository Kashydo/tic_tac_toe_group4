import os
import random
import time
 
 
def main():
    os.system('cls')
    game_mode = menu()
    os.system('cls')
    player = random.randint(1, 2)
    tic = 'X'
    game_board = get_empty_board()
    if game_mode == 1:
        pl_vs_pl(game_board, player, tic)
    elif game_mode == 2:
        rAI_vs_rAI(game_board, player, tic)
    elif game_mode == 3:
        game_board = get_empty_board()
        pl_vs_rAI(game_board, player, tic)
    elif game_mode == 4:
        pl_vs_uAI(game_board, player, tic)
    get_winning_player(game_board)
 
 
# game menu
def menu():
    title()
    print("1. Human vs Human")
    print("")
    print("2. Random AI vs Random AI")
    print("")
    print("3. Human vs Random AI")
    print("")
    print("4. Human vs Unbeatable AI")
    print("")
    print("Quit?")
    print("")
    choice = player_input("Choose your gamemode: ")
    if choice.isdigit() and int(choice) >= 1 and int(choice) <= 4:
        return int(choice)
    else:
        os.system('cls')
        print("Invalid gamemode choice!")
        menu()
 
 
# different game modes:

# player vs player
def pl_vs_pl(board, player, tic):
    while get_winning_player(board) == None:
        title()
        if is_board_full(board):
            print("It's a tie!")
            break
        else:
            display_board(board)
            if player == 1:
                tic = 'X'
                print('Gracz 1')
            elif player == 2:
                tic = "O"
                print("Gracz 2")
            move = ()
            move = get_human_coordinate(board)
            make_a_move(move, board, tic)
            player += 1
            if player == 3:
                player = 1
            os.system('cls')
 
 
# random Ai vs random Ai
def rAI_vs_rAI(board, player, tic):
    while get_winning_player(board) == None:
        title()
        if is_board_full(board):
            print("It's a tie!")
            break
        else:
            display_board(board)
            if player == 1:
                tic = "X"
                print("CPU 1 making a move...")
                move = ()
                move = get_random_ai_coordinate(board)
                time.sleep(2)
                make_a_move(move, board, tic)
            elif player == 2:
                tic = "O"
                print("CPU 2 making a move...")
                move = ()
                move = get_random_ai_coordinate(board)
                time.sleep(2)
                make_a_move(move, board, tic)
            player += 1
            if player == 3:
                player = 1
            os.system('cls')
 
 
# player vs random Ai
def pl_vs_rAI(board, player, tic):
    player = random.randint(1, 2)
    while get_winning_player(board) == None:
        title()
        if is_board_full(board):
            print("It's a tie!")
            break
        else:
            display_board(board)
        # human_cpu = random.randint(1,2)
        if player == 1:
            tic = "X"
            print("Gracz 1")
            move = ()
            move = get_human_coordinate(board)
            make_a_move(move, board, tic)
        elif player == 2:
            tic = "O"
            print("CPU")
            move = ()
            move = get_random_ai_coordinate(board)
            time.sleep(2)
            make_a_move(move, board, tic)
 
        player += 1
        if player == 3:
            player = 1
        os.system('cls')
 
 
# player vs unbeatable Ai
def pl_vs_uAI(board, player, tic):
    while get_winning_player(board) == None:
        title()
        if is_board_full(board):
            print("It's a tie!")
            break
        else:
            display_board(board)
        if player == 1:
            tic = "X"
            print("Gracz 1")
            move = ()
            move = get_human_coordinate(board)
            make_a_move(move, board, tic)
        elif player == 2:
            tic = "O"
            print("CPU")
            move = ()
            move = get_unbeatable_ai_coordinates(board, tic)
            make_a_move(move, board, tic)
        player += 1
        if player == 3:
            player = 1
        os.system('cls')
 
 
# player input and quit
def player_input(prefix):
    a = input(prefix)
    if str(a).upper() == 'QUIT':
        print("Dziękujemy za grę.")
        print('')
        exit()
    else:
        return a
 
 
# ask where to put X/O
def get_human_coordinate(board):
    input_coordinates = player_input(
        "Chose row and column (A1, B2...): ").upper()
    coordinates = list(input_coordinates)
    rows = {'A': 0, 'B': 1, 'C': 2}
    column = {'1': 0, '2': 1, '3': 2}
    try:
        row = int(rows[coordinates[0]])
        col = int(column[coordinates[1]])
    except (IndexError, KeyError):
        print("Invalid move")
        return get_human_coordinate(board)
    if board[row][col] == '.':
        player_move = (row, col)
        return player_move
    else:
        print("Invalid move")
        return get_human_coordinate(board)
 
 
def make_a_move(player_move, board, x_o):
    (row, col) = player_move
    if board[row][col] == ".":
        board[row][col] = x_o
    else:
        print("Invalid move")
 
 
# prepares an empty game board
def get_empty_board():
    empty_board = [['.', '.', '.',], ['.', '.', '.',], ['.', '.', '.',]]
    return empty_board
 
 
# checks if anyone won
def get_winning_player(board):
    row = []
    column = []
    diagonal = []
    rl_diagonal = []
    if check_horizontal(board, row) != None:
        os.system('cls')
        title()
        return check_horizontal(board, row)
    elif check_vertical(board, column) != None:
        os.system('cls')
        title()
        return check_vertical(board, row)
    elif check_diagonal(board, diagonal, rl_diagonal) != None:
        os.system('cls')
        title()
        return check_diagonal(board, diagonal, rl_diagonal)
    else:
        return None
 
 
# wining conditions
def check_horizontal(board, row):
    for i in range(3):
        row = board[i]
        if all(item == 'X' for item in row):
            display_board(board)
            print('X has won!')
            return 'X has won!'
        elif all(item == 'O' for item in row):
            display_board(board)
            print('O has won')
            return 'O has won'
 
 
def check_vertical(board, column):
    for i in range(3):
        column = []
        for j in range(3):
            column.append(board[j][i])
        if all(item == 'X' for item in column):
            display_board(board)
            print('X has won')
            return 'X has won'
        elif all(item == 'O' for item in column):
            display_board(board)
            print('O has won')
            return '0 has won'
 
 
def check_diagonal(board, diagonal, rl_diagonal):
    for i, j in zip(range(3), reversed(range(3))):
        diagonal.append(board[i][i])
        rl_diagonal.append(board[i][j])
    if all(item == 'X' for item in diagonal):
        display_board(board)
        print('X has won')
        return 'X has won'
    elif all(item == 'O' for item in diagonal):
        print('O has won')
        return '0 has won'
    if all(item == 'X' for item in rl_diagonal):
        display_board(board)
        print('X has won')
        return 'X has won'
    elif all(item == 'O' for item in rl_diagonal):
        print('O has won')
        return 'O has won'
 
 
# checks for tie
def is_board_full(board):
    for i in range(3):
        if '.' in board[i]:
            return False
    return True
 
# AI
# Random Ai
def get_random_ai_coordinate(board):
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    if board[row][col] == '.':
        cpu_move = (row, col)
        return cpu_move
    else:
        return get_random_ai_coordinate(board)
 
# unbeatable Ai
def get_unbeatable_ai_coordinates(board, x_o):
    temp_board = board
    for i in range(3):
        for j in range(3):
            if temp_board[i][j] == '.':
                uAI_coordinates = (i, j)
                temp_board[i][j] = 'X'
                if get_winning_player(temp_board) != None:
                    temp_board[i][j] = 'O'
                    return uAI_coordinates
                else:
                    temp_board[i][j] = '.'
    if board[1][1] == ".":
        uAI_coordinates = (1, 1)
        return uAI_coordinates
    for i in range(3):
        for j in range(3):
            if temp_board[i][j] == '.':
                uAI_coordinates = (i, j)
                temp_board[i][j] = x_o
                if get_winning_player(temp_board) != None:
                    return uAI_coordinates
                else:
                    temp_board[i][j] = '.'
    if board[0][0] == ".":
        uAI_coordinates = (0, 0)
        return uAI_coordinates
    elif board[0][2] == ".":
        uAI_coordinates = (0, 2)
        return uAI_coordinates
    elif board[2][0] == ".":
        uAI_coordinates = (2, 0)
        return uAI_coordinates
    elif board[2][2] == ".":
        uAI_coordinates = (2, 2)
        return uAI_coordinates
 
    else:
        return get_random_ai_coordinate(board)
 
# graphics
def title():
    print('\n' +
          ' ________________   _________   ______   __________  ______\n' +
          ' /_  __/  _/ ____/  /_  __/   | / ____/  /_  __/ __ \\/ ____/\n' +
          '  / /  / // /        / / / /| |/ /        / / / / / / __/   \n' +
          ' / / _/ // /___     / / / ___ / /___     / / / /_/ / /___   \n' +
          '/_/ /___/\\____/    /_/ /_/  |_\\____/    /_/  \\____/_____/ \n')
 
 
# displayes edited board with curent game
def display_board(board):
    row_1 = "A" + \
        "| {} | {} | {} |".format(board[0][0], board[0][1], board[0][2])
    row_2 = "B" + \
        "| {} | {} | {} |".format(board[1][0], board[1][1], board[1][2])
    row_3 = "C" + \
        "| {} | {} | {} |".format(board[2][0], board[2][1], board[2][2])
    print('')
    one_two_three = '  1   2   3'
    separetor = "----+---+----"
    print(one_two_three.center(55))
    print(separetor.center(55))
    print(row_1.center(55))
    print(separetor.center(55))
    print(row_2.center(55))
    print(separetor.center(55))
    print(row_3.center(55))
    print(separetor.center(55))
    print('')
 
 
main()