from bots.bot import Bot
from tools.constants import *
from tools.board import *

# add your imports here

class MyBot(Bot):
    """ Maximises the piece point advantage. """
    def heuristic(self, board: Board) -> float:
        """ Implement this method to evaluate the board position. """
        my_colour: Colour=WHITE
        opposition_colour: Colour=BLACK
                
        score = board.get_value(board.get_pieces(colour=my_colour)) - board.get_value(board.get_pieces(colour=opposition_colour))
        return score


    def provide_piece_values(self) -> dict[Piece, float]:
        """ Implement this method to modify the values assigned to each piece. """
        return {
            KING: 0,
            QUEEN: 9,
            ROOK: 5,
            BISHOP: 3,
            KNIGHT: 3,
            PAWN: 1
        }
    
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