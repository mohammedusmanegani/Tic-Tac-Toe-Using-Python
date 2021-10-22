'''''
Author: Mohammed Usman E Gani
Date: 22 October 2021
Problem: Implementation of Tic Tac Toe Game
'''''

# ------- Global Variables -------- #

# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still going
game_still_going = True

# Who  won? or Tie?
winner = None

# Whos turn is it
current_player = "X"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2] + "        1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "        4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "        7 | 8 | 9")


def play_game():
    # Display the initial board
    display_board()

    # while the game is still going
    while game_still_going:
        # Handle a single turn of an arbitary player
        handle_turn(current_player)

        # Check if Game has Ended
        check_if_game_over()

        # Flip To other player
        flip_player()

    if winner == "X" or winner == "0":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


def handle_turn(player):
    # Display whose turn
    print(player + "'s turn.")

    position = input("Choose a position from 1 to 9: ")

    # If you want to exit (Type "exit")
    if position == "exit":
        exit()

    # Input Validation
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1 to 9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there. Go again.")

    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # Setup Global varinables
    global winner

    # Check Rows
    row_winner = check_rows()
    # Check Columns
    column_winner = check_columns()
    # Check Diagonals
    diagonal_winner = check_diagonals()

    # Get the Winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    # Setup global varinables
    global game_still_going

    # check if any of the row has all the same values (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any row dose have a match, Flag that ther is a winner
    if row_1 or row_2 or row_3:
        game_still_going = False

    # Return the winner (X or 0)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # Setup global varinables
    global game_still_going

    # check if any of the column has all the same values (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # If any column dose have a match, Flag that ther is a winner
    if column_1 or column_2 or column_3:
        game_still_going = False

    # Return the winner (X or 0)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    # Setup global varinables
    global game_still_going

    # check if any of the diagonal has all the same values (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    # If any diagonal dose have a match, Flag that ther is a winner
    if diagonal_1 or diagonal_2:
        game_still_going = False

    # Return the winner (X or 0)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "0"
    elif current_player == "0":
        current_player = "X"
    return


# Root Function
play_game()

'''''
All the actions involved in the game are listed below
'''''
# Board
# Display Board
# Play Game
# Handle Turn
# Check if game over
# Check win
# Check Rows
# Check Columns
# Check Diagonals
# Check Tie
# Flip Player
