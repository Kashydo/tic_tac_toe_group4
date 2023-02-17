import os
import random
import time


def main():
    os.system('cls')
    title()
    menu()
    player = 1
    tic = 'X'
    game_board = get_empty_board()
    game_mode = player_input("Choose your gamemode: ")
    if game_mode == '1':
        os.system('cls')
        pl_vs_pl(game_board, player, tic)
    elif game_mode == '2':
        os.system('cls')
        rAI_vs_rAI(game_board, player, tic)
    elif game_mode == '3':
        os.system('cls')
        pl_vs_rAI(game_board, player, tic)
    elif game_mode == '4':
        os.system('cls')
        pl_vs_uAI(game_board, player, tic)
    else:
        game_mode = 0
        print("Invalid choice")
        time.sleep(1)
        main()
    os.system('cls')
    title()
    display_board(game_board)
    if get_winning_player(game_board) == 'X has won':
        print('')
        print('X has won')
    elif get_winning_player(game_board) == 'O has won':
        print('')
        print('X has won')
    print('Dziękujemy za grę')
    print('')


#######################################################################
#######################################################################
# player input and quit


def player_input(d):
    pl_in = input(d)
    if str(pl_in).upper() == 'QUIT':
        print("Dziękujemy za grę.")
        print('')
        quit()
    else:
        return pl_in

#######################################################################
#######################################################################
# difrent game modes
# player vs player


def pl_vs_pl(board, player, tic):
    while get_winning_player(board) == None:
        title()
        if is_board_full(board):
            print("It's a tie!".center(55))
            time.sleep(1)
            break
        else:
            display_board(board)
            if player == 1:
                tic = 'X'
                print('Gracz 1')
            else:
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
            print("It's a tie!".center(55))
            time.sleep(1)
            break
        else:
            display_board(board)
            if player == 1:
                tic = "X"
                print("CPU 1 making a move...")
                move = ()
                move = get_random_ai_coordinate(board)
                time.sleep(1)
                make_a_move(move, board, tic)
            else:
                tic = "O"
                print("CPU 2 making a move...")
                move = ()
                move = get_random_ai_coordinate(board)
                time.sleep(1)
                make_a_move(move, board, tic)
            player += 1
            if player == 3:
                player = 1
            os.system('cls')


# player vs random Ai

def pl_vs_rAI(board, player, tic):
    human_or_cpu = random.randint(1, 2)
    while get_winning_player(board) == None:
        title()
        if is_board_full(board):
            print("It's a tie!".center(55))
            time.sleep(1)
            break
        else:
            display_board(board)
            if player == 1:
                tic = "X"
            else:
                tic = "O"
            if human_or_cpu == 1:
                print("Gracz")
                move = ()
                move = get_human_coordinate(board)
            else:
                print("CPU")
                move = ()
                move = get_random_ai_coordinate(board)
                time.sleep(1)
        human_or_cpu += 1
        make_a_move(move, board, tic)
        player += 1
        if player == 3:
            player = 1
        if human_or_cpu == 3:
            human_or_cpu = 1

        os.system('cls')


# player vs unbitable Ai
def pl_vs_uAI(board, player, tic):
    human_or_cpu = random.randint(1, 2)
    while get_winning_player(board) == None:
        title()
        if is_board_full(board):
            print("It's a tie!".center(55))
            time.sleep(1)
            break
        else:
            display_board(board)
        if player == 1:
            tic = "X"
        else:
            tic = "O"
        if human_or_cpu == 1:
            print("Gracz 1")
            move = ()
            move = get_human_coordinate(board)
        else:
            print("CPU")
            move = ()
            move = get_unbeatable_ai_coordinates(board, tic, 'X', 'O')
        make_a_move(move, board, tic)
        player += 1
        human_or_cpu += 1
        if player == 3:
            player = 1
        if human_or_cpu == 3:
            human_or_cpu = 1
        os.system('cls')


#######################################################################
#######################################################################
# ask where to put X/O


def get_human_coordinate(board):
    input_coordinates = player_input("Chose row and column (A1, B2...): ")
    coordinates = list(input_coordinates.upper())
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

#######################################################################
#######################################################################
# prepers empty game board


def get_empty_board():
    empty_board = [['.', '.', '.',], ['.', '.', '.',], ['.', '.', '.',]]
    return empty_board


#######################################################################
#######################################################################
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
            return 'X has won!'
        elif all(item == 'O' for item in row):
            display_board(board)
            return 'O has won'


def check_vertical(board, column):
    for i in range(3):
        column = []
        for j in range(3):
            column.append(board[j][i])
        if all(item == 'X' for item in column):
            display_board(board)
            return 'X has won'
        elif all(item == 'O' for item in column):
            display_board(board)
            return '0 has won'


def check_diagonal(board, diagonal, rl_diagonal):
    for i, j in zip(range(3), reversed(range(3))):
        diagonal.append(board[i][i])
        rl_diagonal.append(board[i][j])
    if all(item == 'X' for item in diagonal):
        display_board(board)
        return 'X has won'
    elif all(item == 'O' for item in diagonal):
        return '0 has won'
    if all(item == 'X' for item in rl_diagonal):
        display_board(board)
        return 'X has won'
    elif all(item == 'O' for item in rl_diagonal):
        return 'O has won'


#######################################################################
#######################################################################
# check for tie


def is_board_full(board):
    for i in range(3):
        if '.' in board[i]:
            return False
    return True


#######################################################################
#######################################################################
# CPU
# Random Ai


def get_random_ai_coordinate(board):
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    if board[row][col] == '.':
        cpu_move = (row, col)
        return cpu_move
    else:
        return get_random_ai_coordinate(board)


# unbeatable ai


def get_unbeatable_ai_coordinates(board, x_o, x, o):
    time.sleep(1)
    temp_board = board
    for i in range(3):
        for j in range(3):
            if temp_board[i][j] == '.':
                uAI_coordinates = (i, j)
                temp_board[i][j] = x
                if get_winning_player(temp_board) != None:
                    temp_board[i][j] = x_o
                    return uAI_coordinates
                else:
                    temp_board[i][j] = '.'
                temp_board[i][j] = o
                if get_winning_player(temp_board) != None:
                    temp_board[i][j] = x_o
                    return uAI_coordinates
                else:
                    temp_board[i][j] = '.'
    if x_o == 'X' and board[0][0] == ".":
        uAI_coordinates = (0, 0)
        return uAI_coordinates
    else:
        if board[1][1] == '.':
            uAI_coordinates = (1, 1)
        elif board[0][0] == "." and board[0][1] == "." and board[1][0] == ".":
            uAI_coordinates = (0, 0)
        elif board[0][2] == "." and board[1][2] == "." and board[0][1] == ".":
            uAI_coordinates = (0, 2)
        elif board[2][0] == "." and board[2][1] == "." and board[1][0] == ".":
            uAI_coordinates = (2, 0)
        else:
            uAI_coordinates = get_random_ai_coordinate(board)
    return uAI_coordinates


#######################################################################
#######################################################################
# graphics

def title():
    print('\n' +
          '  ________________   _________   ______   __________  ______\n' +
          ' /_  __/  _/ ____/  /_  __/   | / ____/  /_  __/ __ \\/ ____/\n' +
          '  / /  / // /        / / / /| |/ /        / / / / / / __/   \n' +
          ' / / _/ // /___     / / / ___ / /___     / / / /_/ / /___   \n' +
          '/_/ /___/\\____/    /_/ /_/  |_\\____/    /_/  \\____/_____/ \n')


# game menu


def menu():
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


#######################################################################
#######################################################################
main()
