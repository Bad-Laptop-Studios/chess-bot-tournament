""" Dummy main.py. """

import chess
from chessboard import display
from bots.bot import Bot
from tools.board import *
import time

import bots.pawnbot as pawnbot
import bots.piecebot as piecebot
import bots.randobot as randbot
import bots.attackbot as attackbot
import bots.valuebot as valuebot

TURN_DURATION = 2
SEARCH_DEPTH = 3 # must be odd
last_wait_time = time.time()

def main():   
    bot1: Bot = attackbot.MyBot(0)
    bot2: Bot = piecebot.MyBot(1)

    board: Board = Board()

    board_display = display.start(board.fen())
    while not board.is_game_over():
        make_move(board, bot1, board_display)
        if board.is_game_over(): break
        make_move(board, bot2, board_display)
    
    time.sleep(10)

def make_move(board: Board, bot: Bot, board_display):
    best_move = get_evaluation(board, bot, 0)
    board.push(best_move)

    wait_at_least(TURN_DURATION)

    print(best_move)
    display.update(board.fen(), board_display)

    # white_queen = board.get_pieces(QUEEN, WHITE)[0]
    # black_queen = board.get_pieces(QUEEN, BLACK)[0]
    # pieces = board.get_defenders(black_queen.position)
    # for piece in pieces:
    #     position = piece.position.get_alphanumeric()
    #     print(position)

def get_evaluation(board: Board, bot: Bot, current_depth):
    if board.is_game_over():
        return get_game_over_evaluation(board, bot, current_depth)

    if current_depth == SEARCH_DEPTH:
        if bot.bot_id:
            new_board = board.mirror()
            return bot.heuristic(new_board)
        return bot.heuristic(board)
    
    results = {}
    for move in board.legal_moves:
        board.push(move)
        results[move] = get_evaluation(board, bot, current_depth+1)
        board.pop()

    # current_depth = even when it's your move
    if current_depth % 2:
        best_move = min(results, key=results.get)
    else:
        best_move = max(results, key=results.get)

    if current_depth:
        return results[best_move]
    return best_move

def get_game_over_evaluation(board: Board, bot: Bot, current_depth):
    evaluations = bot.provide_game_over_evaluations()
    if board.is_checkmate():
        # current_depth = odd when it's your move
        if current_depth % 2:
            return evaluations["win"] - current_depth # incentivises playing the soonest checkmate
        return evaluations["loss"]
    return evaluations["draw"]

# makes the current move occur at least the given period after the previous
def wait_at_least(period: int):
    global last_wait_time
    current_time = time.time()
    
    time_elapsed = current_time - last_wait_time

    sleep_duration = period - time_elapsed

    if sleep_duration > 0:
        time.sleep(sleep_duration)
    
    last_wait_time = time.time()

if __name__ == "__main__":
    main()