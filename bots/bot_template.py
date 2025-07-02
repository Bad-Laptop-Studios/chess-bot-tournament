from bots.bot import Bot
from tools.constants import *
from tools.board import *

# add your imports here

class MyBot(Bot):
    """ Implement your bot here. """
    def heuristic(self, board: Board) -> float:
        """ Implement this method to evaluate the board position. """
        my_colour: Colour = WHITE
        opposition_colour: Colour = BLACK
        piece_values: dict[Piece, int] = {} # put any overrides to the value of your pieces e.g. {KNIGHT: 4, PAWN: 2}
                                            # feed this into board.get_value()
                                            # e.g. values = board.get_value(my_pieces, piece_values)
        score = 0
        return score
    
    def provide_game_over_evaluations(self) -> dict[str, float]:
        """
        Implement this method to modify the evaluation assigned to each game over state. 
        You should make it so that the evaluation of a draw matches the evaluation your
        heuristic function will return when your bot is in an even position
        """
        return {
            "win": INFINITY,
            "draw": 0,
            "loss": -INFINITY
        }