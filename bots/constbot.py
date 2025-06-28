from chess import Board
from bots.bot_template import Bot
from constants import *

import random

class MyBot(Bot):
    """ Example implementation of Bot. """
    def heuristic(board):
        return 0
    
    def get_values(self) -> dict[str, float]:
        """ This method override is not used by the bot, but it demonstrates that you may override this method too. """
        return {
            KING: 18,
            QUEEN: 9,
            ROOK: 5,
            BISHOP: 3,
            KNIGHT: 3,
            PAWN: 1
        }