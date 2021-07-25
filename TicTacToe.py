# this only works in Jupyter note book from IPython.display import clear_output
import random

def display_board(board):
    # display board
    #clear_output()
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')

def player_input(one_or_two):
    pchoice = ""

    while pchoice.isdigit() == False:

        if one_or_two == 1:
            pchoice = input("Choose a number between 1-9 to place X: ")
            if pchoice.isdigit() == False:  # validate user input
                print("that is not a digit")


        else:
            pchoice = input("Choose a number between 1-9  to place O: ")
            if pchoice.isdigit() == False:
                print("that is not a digit")
    return int(pchoice)  # return player choice to run game function

def place_marker(board, marker, position):

    if marker == 1:  # check if choose_first() returned 1

        board[position] = 'X'  # If choose_first() returns 1 then player 1 is x , place the X on the board

    else:  # player 2 will alaways be O
        marker = 'O'
        board[position] = marker  # place the O on the board

    display_board(board)

def space_check(board, space_check, p_input):

    # this function checks if the position the user has chosen is full, if it does it returns 1 for X and 2 for O
    # if the space is free 3 is returned

    if board[9] == 'X' and p_input == 9:
        print("That space is taken, please choose anohther")
        return 1

    if board[8] == 'X' and p_input == 8:
        print("That space is taken, please choose anohther")

        return 1

    if board[7] == 'X' and p_input == 7:
        print("That space is taken, please choose anohther")

        return 1

    if board[7] == 'X' and p_input == 7:
        print("That space is taken, please choose anohther")

        return 1

    if board[6] == 'X' and p_input == 6:
        print("That space is taken, please choose anohther")

        return 1

    if board[5] == 'X' and p_input == 5:
        print("That space is taken, please choose anohther")

        return 1

    if board[4] == 'X' and p_input == 4:
        print("That space is taken, please choose anohther")

        return 1

    if board[3] == 'X' and p_input == 3:
        print("That space is taken, please choose anohther")

        return 1

    if board[2] == 'X' and p_input == 2:
        print("That space is taken, please choose anohther")

        return 1

    if board[1] == 'X' and p_input == 1:
        print("That space is taken, please choose anohther")

        return 1

    if board[1] == 'O' and p_input == 1:
        print("That space is taken, please choose anohther")

        return 2

    if board[2] == 'O' and p_input == 2:
        print("That space is taken, please choose anohther")

        return 2

    if board[3] == 'O' and p_input == 3:
        print("That space is taken, please choose anohther")

        return 2

    if board[4] == 'O' and p_input == 4:
        print("That space is taken, please choose anohther")

        return 2

    if board[5] == 'O' and p_input == 5:
        print("That space is taken, please choose anohther")

        return 2

    if board[6] == 'O' and p_input == 6:
        print("That space is taken, please choose anohther")

        return 2

    if board[7] == 'O' and p_input == 7:
        print("That space is taken, please choose anohther")

        return 2

    if board[8] == 'O' and p_input == 8:
        print("That space is taken, please choose anohther")

        return 2

    if board[9] == 'O' and p_input == 9:
        print("That space is taken, please choose anohther")

        return 2

    else:

        return 3


def full_board(board):

    if board[9] != '9' and board[8] != '8' and board[7] != '7' and board[6] != '6' and board[5] != '5' and board[
        4] != '4' and board[3] != '3' and board[2] != '2' and board[1] != '1':
        return 1  # check if all board spaces are full and return 1 if true

def replay():
    decision = ''

    while decision not in ('Y', 'N'):

        decision = input('Do you want to play another game? Enter Y for Yes or N for no ')
        if decision == 'Y':
            return True




        else:
            return False

def choose_first():
     player1 = 1
     player2 = 2

     check = random.randint(1, 2)
     if check == 1:
         print('Player 1 goes first!')
         return player1
     else:
         print('Random generator chose 2 so player 2 goes first!')
         return player2


def whos_go(one_or_two):
    if one_or_two == 1:
        return 2
    else:
        return 1


def win_check(board, game_won):
    if board[9] == 'X' and board[8] == 'X' and board[7] == 'X':
        print("Player 1 is the winner!")
        return True

    if board[6] == 'X' and board[5] == 'X' and board[4] == 'X':
        print("Player 1 is the winner!")
        return True

    if board[3] == 'X' and board[2] == 'X' and board[1] == 'X':
        print("Player 1 is the winner!")
        return True

    if board[3] == 'X' and board[5] == 'X' and board[7] == 'X':
        print("Player 1 is the winner!")
        return True

    if board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        print("Player 1 is the winner!")
        return True

    if board[9] == 'X' and board[6] == 'X' and board[3] == 'X':
        print("Player 1 is the winner!")
        return True

    if board[9] == 'X' and board[5] == 'X' and board[1] == 'X':
        print("Player 1 is the winner!")
        return True

    if board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        print("Player 1 is the winner!")
        return True

    if board[9] == 'O' and board[8] == 'O' and board[7] == 'O':
        print("Player 2 is the winner!")
        return True

    if board[6] == 'O' and board[5] == 'O' and board[4] == 'O':
        print("Player 2 is the winner!")
        return True

    if board[3] == 'O' and board[2] == 'O' and board[1] == 'O':
        print("Player 2 is the winner!")
        return True

    if board[3] == 'O' and board[5] == 'O' and board[7] == 'O':
        print("Player 2 is the winner!")
        return True

    if board[9] == 'O' and board[5] == 'O' and board[1] == 'O':
        print("Player 2 is the winner!")
        return True

    if board[8] == 'O' and board[5] == 'O' and board[2] == 'O':
        print("Player 2 is the winner!")
        return True

    if board[7] == 'O' and board[4] == 'O' and board[1] == 'O':
        print("Player 2 is the winner!")
        return True

    if board[9] == 'O' and board[6] == 'O' and board[3] == 'O':
        print("Player 2 is the winner!")

        return True
    else:
        return False

while True:


    print('Welcome')
    board = [" # ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    check_space = 3
    p_input = 0

    player_position = choose_first()
    print('player position is ', player_position)

    # if 3>7:
    # game_over=True
    # else:
    # game_over=False

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_over = False
    else:
        game_over = True

    while game_over == False:
        display_board(board)
        p_input = player_input(player_position)
        check_space = space_check(board, check_space, p_input)
        if check_space == 1 or check_space == 2:

           check_space = 0  # reset check space variable
           continue  # if check space returns 1 or 2 that means the space is taken and then continue cause the player_input() function to be called again
        else:
            place_marker(board, player_position, p_input)

            player_position = whos_go(player_position)
            # print("Check space is initially ", check_space)
            game_over = win_check(board, game_over)
            check_space = 0 # reset check_space to 0
            full = full_board(board)
            if full == 1 and game_over==False:  # check for a full board and no winner

                print("Stalemate!")

    if not replay():
        break



