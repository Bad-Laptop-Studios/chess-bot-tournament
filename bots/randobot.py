from chess import Board
from bots.bot_template import Bot

import random

class MyBot(Bot):
    """ Example implementation of Bot. """
    def heuristic(self, board: Board) -> float:
        return random.random()
