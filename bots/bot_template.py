from chess import Board
from bots.bot_template import Bot
from tools.constants import *

# add your imports here

class MyBot(Bot):
    """ Implement your bot here. """
    def heuristic(self, board: Board) -> float:
        """ Implement this method to evaluate the board position. """
        return 0


    def get_values(self) -> dict[Piece, float]:
        """ Implement this method to modify the values assigned to each piece. """
        return {
            KING: 18,
            QUEEN: 9,
            ROOK: 5,
            BISHOP: 3,
            KNIGHT: 3,
            PAWN: 1
        }