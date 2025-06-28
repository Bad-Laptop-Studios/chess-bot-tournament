from chess import Board
from constants import *

class Analyser():
    def get_positions(board: Board, colour: Colour, piece: Piece) -> list[Position]:
        """
        >>> board = chess.Board()
        >>> get_positions(board, WHITE, QUEEN)
        ['d1']
        >>> get_positions(board, WHITE, ROOK)
        ['a1', 'h1']
        >>> get_positions(board, WHITE, PAWN)
        ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']
        >>> get_positions(board, BLACK, QUEEN)
        ['d8']
        
        """
        pass

    def position_attacks(board: Board, colour: Colour, position: Position, piece: Piece=None) -> list[(Position, Piece)] | None:
        """
        >>> board = chess.Board()
        >>> position_attacks(board, WHITE, 'a1')
        []
        >>> position_attacks(board, WHITE, 'd4')
        None                                        # no piece at d4
        >>> move(board, WHITE, 'd2d3')              # not a real function
        >>> move(board, WHITE, 'c1h6')
        >>> position_attacks(board, WHITE, 'h6')
        ['g7']

        >>> position_attacks(board, WHITE, 'd6', QUEEN)
        ['c7', 'd7', 'e7']
        >>> position_attacks(board, WHITE, 'd6', KNIGHT)
        ['b7', 'c8', 'e8', 'f7']
        """
        pass

