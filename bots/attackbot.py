from bots.bot import Bot
from tools.constants import *
from tools.board import *
from tools.heat_maps import *

# add your imports here

class MyBot(Bot):
    """ Implement your bot here. """
    def heuristic(self, board: Board) -> float:
        """ Implement this method to evaluate the board position. """
        my_colour: Colour = WHITE
        opposition_colour: Colour = BLACK
        piece_values: dict[Piece, int] = {}

        my_piece_values = board.get_value(board.get_pieces(my_colour))
        opposition_piece_values = board.get_value(board.get_pieces(opposition_colour))

        my_pawns = board.get_pieces(PAWN, my_colour)
        my_pawns_score = find_positional_value(my_pawns, STAIRWAY, 0.1)

        opposition_pawns = board.get_pieces(PAWN, opposition_colour)
        opposition_pawns_score = find_positional_value(opposition_pawns, REVERSE_STAIRWAY, -0.1)

        my_minors = board.get_pieces([KNIGHT, BISHOP], my_colour)
        NEW_CENTRE = meta_element_addition(CENTRE, -2)
        my_minors_score = find_positional_value(my_minors, NEW_CENTRE, 0.1)

        total_attacked = 0
        my_pieces = board.get_pieces(my_colour)
        for piece in my_pieces:
            attacked_pieces = board.get_attacks(piece.position)
            total_attacked += len(attacked_pieces)
        attack_score = total_attacked * 0.02

        hanging_value = 0
        for piece in my_pieces:
            attackers = len(board.get_attackers(piece.position))
            defenders = len(board.get_defenders(piece.position))
            if attackers > defenders:
                hanging_value += board.get_value([piece])

        score = 0
        score += my_piece_values - opposition_piece_values
        score += my_pawns_score - opposition_pawns_score
        score += my_minors_score
        score += attack_score
        score -= hanging_value
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