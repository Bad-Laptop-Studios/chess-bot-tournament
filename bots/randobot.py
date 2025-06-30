from chess import Board as ChessBoard
from bots.bot_template import Bot

import random


class MyBot(Bot):
    """ Example implementation of Bot. """
    def heuristic(self, board: ChessBoard) -> float:
        return random.random()
