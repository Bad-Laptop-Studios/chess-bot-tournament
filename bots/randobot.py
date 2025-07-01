from bots.bot_template import Bot
from tools.board import *

import random


class MyBot(Bot):
    """ Example implementation of Bot. """
    def heuristic(self, board: Board) -> float:
        return random.random()