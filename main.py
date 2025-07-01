""" Dummy main.py. """

import chess
from chessboard import display
from bots.bot import Bot
from tools.board import *
import time
import copy

import bots.randobot as randobot
import bots.constbot as constbot
import bots.valuebot as valuebot

TURN_DURATION = 1
SEARCH_DEPTH = 3 # must be odd

def main():   
    bot1: Bot = randobot.MyBot(0)
    bot2: Bot = valuebot.MyBot(1)

    board: Board = Board()
    piece_values = [bot1.provide_piece_values(), bot2.provide_piece_values()]

    board_display = display.start(board.fen())
    while not board.is_game_over():
        make_move(board, bot1, board_display, piece_values)
        make_move(board, bot2, board_display, piece_values)
        display.update(board.fen(), board_display)
        # display.terminate

def make_move(board: Board, bot: Bot, board_display, piece_values):
    board.retrieve_piece_values(piece_values[bot.bot_id])

    best_move = get_evaluation(board, bot, 0)
    board.push(best_move)
    print(best_move)
    display.update(board.fen(), board_display)
    
    time.sleep(TURN_DURATION)

def get_evaluation(board: Board, bot: Bot, current_depth):
    if board.is_game_over():
        return get_game_over_evaluation(board, bot, current_depth)

    if current_depth == SEARCH_DEPTH:
        if bot.bot_id:

            new_board = board.mirror()
            new_board.piece_values = board.piece_values
            return bot.heuristic(new_board)
        return bot.heuristic(board)
    
    results = {}
    for move in board.legal_moves:
        board.push(move)
        results[move] = get_evaluation(board, bot, current_depth+1)
        board.pop()

    if current_depth % 2 == 0:
        best_move = min(results, key=results.get)
    else:
        best_move = max(results, key=results.get)

    if current_depth:
        return results[best_move]
    return best_move

def get_game_over_evaluation(board: Board, bot: Bot, current_depth):
    evaluations = bot.provide_game_over_evaluations()
    if board.is_checkmate():
        if current_depth % 2 == 0:
            return evaluations["win"]
        return evaluations["loss"]
    return evaluations["draw"]

if __name__ == "__main__":
    main()