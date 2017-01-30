#!/usr/bin/env python3


# empty board list
lst_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def display_board(board):
    """
    Draws a board in 3x3 field format. Takes input from 'board' list.
    """
    # draws a board, prints board list in three rows
    print("\n", board[0], board[1], board[2], "\n",
          board[3], board[4], board[5], "\n",
          board[6], board[7], board[8], "\n")


def player_input():
    """
    Takes input from player. Needs board as a list input.
    Returns a player played position from 1-9.
    """
    entry = ""
    while entry not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        entry = input("Enter a field number (1-9)?")

    return int(entry)


def place_marker(board, marker, position):
    """Takes a position and marks it on the board"""
    for index, item in enumerate(board):  # goes through list
        if item == position:  # checks if player response is in board list
            board[index] = marker  # places marker, X or O in position played
    return board  # returns new board list with the marker player played


def win_check(board, mark):
    """
    :param board: Takes in board list
    :param mark: Takes in player mark, X or O
    :return: Checks who has 3 marks in a row, who has won
    """
    if mark == board[0] and mark == board[1] and mark == board[2]:
        return mark
    elif mark == board[3] and mark == board[4] and mark == board[5]:
        return mark
    elif mark == board[6] and mark == board[7] and mark == board[8]:
        return mark
    elif mark == board[2] and mark == board[4] and mark == board[6]:
        return mark
    elif mark == board[0] and mark == board[4] and mark == board[8]:
        return mark
    elif mark == board[0] and mark == board[3] and mark == board[6]:
        return mark
    elif mark == board[1] and mark == board[4] and mark == board[7]:
        return mark
    elif mark == board[2] and mark == board[5] and mark == board[8]:
        return mark
    else:
        return False


def is_tie(lst):
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if any(s in lst for s in test):  # any with generator
        print("Continue")
    else:
        print("It's a tie. Game Over!")
        return True


display_board(lst_board)  # displays the board
while True:
    # player1 game
    ent1 = player_input()  # player input
    plc = place_marker(lst_board, "X", ent1)  # board with the player marker
    wc1 = win_check(lst_board, "X")
    if wc1 == "X":
        print("Player 1 won!")
        break
    else:
        print("No win yet, continue\n")

    display_board(lst_board)  # displays the board
    is_tie(lst_board)

    # player2 game
    ent2 = player_input()  # player input
    plc2 = place_marker(lst_board, "O", ent2)  # board with the player marker
    wc2 = win_check(lst_board, "O")
    if wc2 == "O":
        print("Player 2 won!")
        break
    else:
        print("No win yet, continue\n")

    display_board(lst_board)  # displays the board
    is_tie(lst_board)
