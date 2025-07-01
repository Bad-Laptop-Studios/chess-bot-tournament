""" Dummy main.py. """

import chess
from chessboard import display
from bots.bot import Bot
import time
import copy

import bots.randobot as randobot
import bots.constbot as constbot

TURN_DURATION = 1
SEARCH_DEPTH = 3 # must be odd

def main():
    board: chess.Board = chess.Board()

    bot1: Bot = randobot.MyBot()
    bot2: Bot = constbot.MyBot()

    while not board.is_game_over():
        board_display = display.start(board.fen())
        for i in range(10):
            make_move(board, board_display, bot1)
            make_move(board, board_display, bot2)
        # display.terminate

def make_move(board: chess.Board, board_display, bot: Bot):
    best_move = get_evaluation(board, bot, 0)

    board.push(best_move)
    print(best_move)
    display.update(board.fen(), board_display)

    time.sleep(TURN_DURATION)

def get_evaluation(board: chess.Board, bot: Bot, current_depth):
    if board.is_game_over():
        return get_game_over_evaluation(board, bot, current_depth)

    if current_depth == SEARCH_DEPTH:
        return bot.heuristic(board)
    
    results = {}
    for move in board.legal_moves:
        new_board = copy.copy(board)
        new_board.push(move)
        results[move] = get_evaluation(new_board, bot, current_depth+1)

    if current_depth % 2 == 0:
        best_move = min(results, key=results.get)
    else:
        best_move = max(results, key=results.get)

    if current_depth:
        return results[best_move]
    return best_move

def get_game_over_evaluation(board: chess.Board, bot: Bot, current_depth):
    evaluations = bot.get_game_over_evaluations()
    if board.is_checkmate():
        if current_depth % 2 == 0:
            return evaluations["win"]
        return evaluations["loss"]
    return evaluations["draw"]

if __name__ == "__main__":
    main()