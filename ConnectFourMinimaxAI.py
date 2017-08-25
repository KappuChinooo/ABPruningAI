import copy
import ConnectFourBoard
import random
import time

def other(token):
    if token == ConnectFourBoard.RED:
        return ConnectFourBoard.BLUE
    elif token == ConnectFourBoard.BLUE:
        return ConnectFourBoard.RED
    else:
        return None


# estimate of a field quality
def state_score(board, turn):
    (red, blue) = board.score()
    if turn == ConnectFourBoard.RED:
        return red - blue
    else:
        return blue - red


def max_play(board, token, ply_remaining):
    moves = []
    for col in board.not_full_columns():
        newboard = board.copy()
        newboard.attempt_insert(col, token)
        if ply_remaining <= 0 or newboard.is_full():
            value = state_score(newboard, token)
        else:
            (min_move, value) = min_play(newboard, token, ply_remaining-1)
        moves.append((col, value))
    random.shuffle(moves)
    move = max(moves, key = lambda x: x[1])
    return move

def AIcheck(board, token):
    # Modify to set a different search depth
    starttime = time.time()
    ply_remaining = 3
    (move, value) = max_play(board, token, ply_remaining)
    endtime = time.time()
    tkn = endtime - starttime
    txt = open("text.txt","a")
    txt.write(str(tkn) + " MNM"+ '\n')
    txt.close()
    return move

def min_play(board, token, ply_remaining):
    moves = []
    for col in board.not_full_columns():
        newboard = board.copy()
        newboard.attempt_insert(col, token)
        if ply_remaining <= 0 or newboard.is_full():
            value = state_score(newboard, token)
        else:
            (max_move, value) = max_play(newboard, token, ply_remaining-1)
        moves.append((col, value))
    random.shuffle(moves)
    move = min(moves, key = lambda x: x[1])
    return move
