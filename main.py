""" Dummy main.py. """

import chess
from chessboard import display
from bots.bot import Bot
import time

import bots.randobot as randobot
import bots.constbot as constbot

board: chess.Board = chess.Board()

bot1: Bot = randobot.Bot()
bot2: Bot = constbot.Bot()

TURN_DURATION = 1

def main():
    # while not board.is_checkmate():
    board_display = display.start(board.fen())
    for i in range(10):
        make_move(board, board_display, bot1)
        make_move(board, board_display, bot2)
    display.terminate

def make_move(board: chess.Board, board_display, bot: Bot):
    results = {}
    for move in board.legal_moves:
        results[move] = bot.heuristic()

    best_move = max(results, key=results.get)

    board.push(best_move)
    print(best_move)
    display.update(board.fen(), board_display)

    time.sleep(TURN_DURATION)


if __name__ == "__main__":
    main()