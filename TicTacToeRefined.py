# only works in Jupyter notebook from IPython.display import clear_output
import random


def display_board(board): # print the board layoung and list positions
    # only works in Jupyter notebook   clear_output()

    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'): # while loop is used incase the user does not input an X or O
        marker = input('Player 1 do you want to be X or O?') # ask the user for input

    if marker == 'X'.upper():
        return ('X', 'O') # return tuple

    else:
        return ('O', 'X') # if user chose O then O is first to be returned in the tuple


def place_marker(board, marker, position):
    board[position] = marker # place the X or O on the board at the position chosen by the user


def space_check(board, position):
    # print(board[position]=="X" or board[position]=="O")
    return board[position] != 'X' and board[position] != "O" # check and return true if the position in the board is not an X or O


def choose_first(): # function to choose which player goes first using the randint function from the random class


    check = random.randint(1, 2)
    if check == 1:
        print('Player 1 goes first!')
        return 1
    else:
        print('Player 2 goes first!')
        return 2

def full_board_check(board):
    for i in range(len(board)): # check each position in board and  check if it it is filled
        if space_check(board, i): #  space_check checks if a   board position is not equal to X or O and if so returns True
                # used for testing  print(i)
            return False # if space is not X or O full board is false
       # used for testing print(i)
        return True # if it is full return true  - this return is outside of the loop so it only returns true once all board positions are checked


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


def win_check(board, mark):
    return ((board[9] == mark and board[8] == mark and board[7] == mark) or # check for winner accross the top
            (board[6] == mark and board[5] == mark and board[4] == mark) or # check for winner accross the  middle
            (board[3] == mark and board[2] == mark and board[1] == mark) or # check for winner accross the bottom
            (board[3] == mark and board[5] == mark and board[7] == mark) or # check for winner diagonally
            (board[2] == mark and board[5] == mark and board[8] == mark) or # check for winner down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or # check for winner down the right
            (board[9] == mark and board[5] == mark and board[1] == mark) or # check for winner diagonally the opposite way
            (board[7] == mark and board[4] == mark and board[1] == mark)) # check for winner down the left


# below is the code that runs the game logic
print("Welcome to Tic-Tac-Toe!")
while True:
    board = [" # ", "1", "2", "3", "4", "5", "6", "7", "8", "9"] #set up the board


    player1_marker, player2_marker = player_input() # use tuple unpacking to set the player variable to X or O
    turn = choose_first() # use the random function to and set it to variable "turn" to hold value of who goes first
    print(turn, ' will go first')

    play_game = input("Are you ready to play? Enter Yes or No")
    if play_game.lower()[0] == 'y':
        game_on = True # if the player is ready set game_on to true which then triggers the while loop below
    else:
        game_on = False


    while game_on:
        if turn == 1: # if its player 1's go

            display_board(board)
            print('Player 1 place your' , player1_marker) # tell player 1 to place their marker
            position = player_choice(board) # call player_choice function which will get the user input and set it to variable position
            place_marker(board, player1_marker, position) # call the place_marker function and pass in board, player1_marker and the position the user has chosen above

            if win_check(board, player1_marker):# check if the move above has won the game
                display_board(board)
                print("Player 1 wins!") # if player 1 has won
                game_on = False # if the game is won then this will close the while loop
            else:
                if full_board_check(board) and game_on==False: # check if the board is full and there hasn't been a winner
                    display_board(board)
                    print("Stalemate")
                    break
                else:
                    turn = 2 # set player turn   to 2

        else:

            display_board(board)
            print('Player 2 your place your', player2_marker) #tell player 1 to place their marker
            position = player_choice(board) # call player_choice function which will get the user input and set it to variable position
            place_marker(board, player2_marker, position) # call the place_marker function and pass in board, player1_marker and the position the user has chosen above

            if win_check(board, player2_marker): # check if the move above has won the game
                display_board(board)
                print("Player 2 wins!") # if player 2 has won
                game_on = False # if the game is won then this will close the while loop
            else:
                if full_board_check(board) and game_on==False:  # check if the board is full and there hasn't been a winner
                    display_board(board)
                    print("Stalemate")
                    break
                else:

                    turn = 1  #set player turn back 1

    if not replay(): # if players do not want to replay then break out of the loop, if they do want to replay the game resets
        break
