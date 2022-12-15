# pylint: disable=broad-except
# pylint: disable=unused-variable
# pylint: disable=consider-using-enumerate
import os

RED = "\033[2;31;1mR\033[0;0m"
YELLOW = "\033[2;33;1mY\033[0;0m"


def is_board_valid(board):
    """checks if the given board is a list and has a length of 7"""
    return isinstance(board, list) and len(board) == 7


def print_board(board):
    # pylint: disable=consider-using-enumerate
    """prints the board to the console"""
    try:
        if is_board_valid(board):
            header = ' '
            # for each column of the board (range 0 to length of 2D array) add number to header
            # len(board)+1 because we want columns from 1 to 7 and not from 1 to 6
            for number in range(1, len(board)+1):
                header += ' ' + str(number) + '  '
            print(header)
            # print top line of board
            print('+---' * (len(board)) + '+')

            # Printing each row of the board
            for row in range(len(board[0])):
                row_with_items = ''
                for column in range(len(board)):
                    row_with_items += f'| {str(board[column][row])} '
                print(row_with_items + '|')
                print('+---' * (len(board)) + '+')
        else:
            print("Invalid board")
    except Exception as exception:
        print(exception)


def is_move_valid(board, move):
    """checks if a given move is valid"""
    try:
        if isinstance(board, list):
            if len(board) < 7:
                print("Board has not enough columns")
                return False
        else:
            print("Did not recieve array as input parameter")
            return False

        if isinstance(move, int):
            if move < 1 or move > len(board):
                print(
                    f"Please select a valid column between 1 and {len(board)}")
                return False

            #column is full
            if board[move-1][0] != " ":
                print(
                    f"Make sure to pick a column between 1 and {len(board)} that is not full")
                return False
        else:
            print("Move is not a number")
            return False

        return True
    except Exception as exception:
        print(exception)
        return False


def place_piece(board, column, player):
    """places a piece into the desired slot on the board"""
    try:
        if is_board_valid(board):
            if not is_move_valid(board, column):
                print("Move not valid")
                return False

            # Places a piece at the bottom of the selected column
            for slot in range(len(board[0])-1, -1, -1):
                if board[column-1][slot] == ' ':
                    board[column-1][slot] = player
                    return True
        else:
            print("Invalid board")
            return False
    except Exception as exception:
        print(exception)
        return False


def get_available_moves(board):
    """return the available moves that can be made by the player"""
    moves = []
    try:
        # Returns the columns that are open

        for i in range(1, len(board)+1):
            if is_move_valid(board, i):
                moves.append(i)

    except Exception as exception:
        print(exception)
    return moves


def has_won(board, symbol):
    """Return True if any player has won the game"""
    try:
        if len(board) == 7:
            # check horizontal spaces
            for row in range(len(board[0])):
                for column in range(len(board) - 3):
                    if board[row][column] == symbol and board[row+1][column] == symbol and board[row+2][column] == symbol and board[row+3][column] == symbol:
                        return True

            # check vertical spaces
            for row in range(len(board)):
                for column in range(len(board[0]) - 3):
                    if board[row][column] == symbol and board[row][column+1] == symbol and board[row][column+2] == symbol and board[row][column+3] == symbol:
                        return True

            # check / diagonal spaces
            for row in range(len(board) - 3):
                for column in range(3, len(board[0])):
                    if board[row][column] == symbol and board[row+1][column-1] == symbol and board[row+2][column-2] == symbol and board[row+3][column-3] == symbol:
                        return True

            # check \ diagonal spaces
            for row in range(len(board) - 3):
                for column in range(len(board[0]) - 3):
                    if board[row][column] == symbol and board[row+1][column+1] == symbol and board[row+2][column+2] == symbol and board[row+3][column+3] == symbol:
                        return True

        return False
    except Exception as exception:
        print(exception)
    return False


def game_is_over(board):
    """Calls the has_won function to see if any player has won or the game is a tie"""
    try:
        # Returns True if either player has won the game or if there are no open columns
        return has_won(board, RED) or has_won(board, YELLOW) or len(get_available_moves(board)) == 0
    except Exception as exception:
        print(exception)
        # return True so the game ends if something gets caught by the try block
        return True


def play_game():
    """Calls all previously mentioned functions to play the game"""
    try:
        # clearing the console
        os.system("clear")
        # Creating an empty board
        board = []
        for column in range(7):
            board.append([' '] * 6)

        # Starting the game with Red going first
        player = RED
        winner = False
        while not game_is_over(board):
            print_board(board)
            move = 0
            available_moves = get_available_moves(board)
            # Continuing to ask for a valid move until the user gives one
            while (move not in available_moves):
                try:
                    move = int(input(
                        f"It is {player}'s turn. Please select a column between 1 and {int(len(board))}: "))
                    is_move_valid(board, move)
                except Exception as exception:
                    print(f"Please enter a valid number: {exception}")
                    continue
            place_piece(board, move, player)
            # Checking to see if this move wins the game for the player. If so, exiting the loop
            if has_won(board, player):
                os.system("clear")
                print_board(board)
                print(f"{player} has won!")
                winner = True
                break

            # Switching the players turn
            if player == RED:
                player = YELLOW
            else:
                player = RED

            os.system("clear")
        # If we exit the loop and haven't determined a winner, that means it was a tie
        if not winner:
            print("It was a tie!")
            print_board(board)
    except Exception as exception:
        print(exception)


if __name__ == "__main__":
    play_game()
