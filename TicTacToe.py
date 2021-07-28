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


def whos_go(one_or_two): # determine which players go it is
    if one_or_two == 1: # if player 1 has had his go
        return 2 # it is now player 2's go
    else:
        return 1


def win_check(board, game_won): # function to check if game has been won
    if board[9] == 'X' and board[8] == 'X' and board[7] == 'X': # across the top
        print("Player 1 is the winner!")
        return True

    if board[6] == 'X' and board[5] == 'X' and board[4] == 'X': # across the middle
        print("Player 1 is the winner!")
        return True

    if board[3] == 'X' and board[2] == 'X' and board[1] == 'X': # accross the bottom
        print("Player 1 is the winner!")
        return True

    if board[3] == 'X' and board[5] == 'X' and board[7] == 'X': # diagonally
        print("Player 1 is the winner!")
        return True

    if board[2] == 'X' and board[5] == 'X' and board[8] == 'X': # down the middle
        print("Player 1 is the winner!")
        return True

    if board[9] == 'X' and board[6] == 'X' and board[3] == 'X': # down the right side
        print("Player 1 is the winner!")
        return True

    if board[9] == 'X' and board[5] == 'X' and board[1] == 'X': #diagonally the opposite way
        print("Player 1 is the winner!")
        return True

    if board[1] == 'X' and board[4] == 'X' and board[7] == 'X': # up the left
        print("Player 1 is the winner!")
        return True

    if board[9] == 'O' and board[8] == 'O' and board[7] == 'O': # across the top
        print("Player 2 is the winner!")
        return True

    if board[6] == 'O' and board[5] == 'O' and board[4] == 'O': # across the middle
        print("Player 2 is the winner!")
        return True

    if board[3] == 'O' and board[2] == 'O' and board[1] == 'O': # across the bottom
        print("Player 2 is the winner!")
        return True

    if board[3] == 'O' and board[5] == 'O' and board[7] == 'O': # diagonally
        print("Player 2 is the winner!")
        return True

    if board[9] == 'O' and board[5] == 'O' and board[1] == 'O': # diagonally the other way
        print("Player 2 is the winner!")
        return True

    if board[8] == 'O' and board[5] == 'O' and board[2] == 'O': # down the middle
        print("Player 2 is the winner!")
        return True

    if board[7] == 'O' and board[4] == 'O' and board[1] == 'O': # down the left side
        print("Player 2 is the winner!")
        return True

    if board[9] == 'O' and board[6] == 'O' and board[3] == 'O': # down the right side
        print("Player 2 is the winner!")

        return True
    else:
        return False

while True: # logic code to run the game


    print('Welcome')
    board = [" # ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    check_space = 3 # set the check space variable
    p_input = 0 # set the p_input variable

    player = choose_first() # set player_position to choose first which chooses who goes first
    #print('player position is ', player)



    play_game = input('Are you ready to play? Enter Yes or No.') # ask the user if they are ready to play

    if play_game.lower()[0] == 'y': # if the first letter of input is y then set game_over to false which triggers the while loop
        game_over = False
    else:
        game_over = True

    while game_over == False:
        display_board(board) # display the game board
        p_input = player_input(player) # pass the player  variable into the player_input function and set it to p_input. If player_position is set to 1 then an X will be placed, otherwise O will be placed.
        check_space = space_check(board, check_space, p_input) # check to see if the space that the user has chosen is free
        if check_space == 1 or check_space == 2:

           check_space = 0  # reset check space variable if a space is full
           continue  # if check space returns 1 or 2 that means the space is taken and then continue cause the player_input() function to be called again
        else:
            place_marker(board, player, p_input) # if the space is free put the marker on the board

            player = whos_go(player) # call the whos_go function and it set it to player
            # print("Check space is initially ", check_space)
            game_over = win_check(board, game_over)
            check_space = 0 # reset check_space to 0
            full = full_board(board)
            if full == 1 and game_over==False:  # check for a full board and no winner

                print("Stalemate!")

    if not replay(): # if the user does not want to replay break out of the loop
        break



