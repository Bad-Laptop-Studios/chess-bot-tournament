from bots.bot import Bot
from tools.constants import *
from tools.board import *
from tools.heat_maps import *
import random

# add your imports here

class MyBot(Bot):
    """ Implement your bot here. """
    def heuristic(self, board: Board) -> float:
        """ Bot likes to push pawns. """
        my_colour: Colour=WHITE
        opposition_colour: Colour=BLACK

        my_pawns = board.get_pieces(PAWN, my_colour)
        my_pawns_score = find_positional_value(my_pawns, STAIRWAY, 0.1)

        opposition_pawns = board.get_pieces(PAWN, opposition_colour)
        opposition_pawns_score = find_positional_value(opposition_pawns, REVERSE_STAIRWAY, -0.1)

        value_difference = board.get_value(board.get_pieces(colour=my_colour)) - board.get_value(board.get_pieces(colour=opposition_colour))

        my_minors = board.get_pieces([KNIGHT, BISHOP], my_colour)
        NEW_CENTRE = meta_element_addition(CENTRE, -2)
        my_minors_score = find_positional_value(my_minors, NEW_CENTRE, 0.1)

        score = 0
        score += my_pawns_score
        score += opposition_pawns_score
        score += value_difference
        score += my_minors_score

        return score + random.random() / 100


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