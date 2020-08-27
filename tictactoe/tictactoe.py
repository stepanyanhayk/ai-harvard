"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for row in board:
        for square in row:
            if square is not EMPTY:
                count += 1

    if count % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for row in range(len(board)):
        for square in range(len(board[row])):
            if board[row][square] is EMPTY:
                moves.add((row, square))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    if board_copy[action[0]][action[1]] != EMPTY:
        raise IndexError
    else:
        board_copy[action[0]][action[1]] = player(board_copy)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Checking rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]

    # Checking columns
    for column_ind in range(3):
        if board[0][column_ind] == board[1][column_ind] == board[2][column_ind] and board[0][column_ind] != 0:
            return board[0][column_ind]

    # Checking diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != EMPTY:
        return board[1][1]
    if board[2][0] == board[1][1] == board[0][2] and board[1][1] != EMPTY:
        return board[1][1]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None:
        count = 0
        for row in board:
            for square in row:
                if square is not EMPTY:
                    count += 1
        if count == 9:
            return True
        else:
            return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def max_value(state):
    if terminal(state):
        return utility(state)
    v = -math.inf
    for action in actions(state):
        v = max(v, min_value(result(state, action)))
    return v


def min_value(state):
    if terminal(state):
        return utility(state)
    v = math.inf
    for action in actions(state):
        v = min(v, max_value(result(state, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        best_value = -1
        best_move = None
        for action in actions(board):
            v = min_value(result(board, action))
            if v > best_value:
                best_value = v
                best_move = action
    else:
        best_value = 1
        best_move = None
        for action in actions(board):
            v = max_value(result(board, action))
            if v < best_value:
                best_value = v
                best_move = action
    return best_move
