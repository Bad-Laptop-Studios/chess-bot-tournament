import chess
from chess import Board as ChessBoard
from tools.constants import *

from dataclasses import dataclass

from multipledispatch import dispatch


class Position:
    """
    >>> alpha = Position("a2")
    >>> alpha.get_alpha()
    "a2"
    >>> alpha.get_vector()
    (2, 1)
    >>> print(alpha)
    a2
    >>> vector = Position(2, 3)
    >>> vector.get_alpha()
    "c2"
    >>> vector.get_vector()
    (2, 3)
    >>> print(vector)
    c2
    """
    @dispatch(str)
    def __init__(self, file_rank: str):
        """"""
        if not len(file_rank) == 2:
            pass    # TODO
        self.row = 1
        self.col = 1  

    @dispatch(int, int)
    def __init__(self, row: int, col: int):
        """3,5"""
        self.row = row
        self.col = col

    @dispatch(int)
    def __init__(self, square: int):
        self.row = chess.square_rank(square) + 1
        self.col = chess.square_file(square) + 1

    COLUMN_LOOKUP = "abcdefgh"

    def __str__(self):
        return self.get_alphanumeric()
    
    def get_alphanumeric(self) -> PositionAlpha:
        return self.COLUMN_LOOKUP[self.col - 1] + str(self.row)
    
    def get_vector(self) -> PositionVector:
        return self.row, self.col


class Piece:
    """TODO."""
    @dispatch(PieceType, Colour, Position)
    def __init__(self, type: PieceType, colour: Colour, position: Position) -> None:
        self.type: PieceType = type
        self.colour: Colour = colour
        self.position: Position = position

                                               # PositionVector
    # @dispatch(PieceType, Colour, PositionAlpha | tuple)
    # def __init__(self, type: PieceType, colour: Colour, position: PositionAlpha) -> None:
    #     self.type: PieceType = type
    #     self.colour: Colour = colour
    #     self.position: Position = Position(position)

    # The above didn't seem to work because of 'PositionAlpha | tuple' so I duplicated it and seperated the PositionAlpha and tuple
    @dispatch(PieceType, Colour, PositionAlpha)
    def __init__(self, type: PieceType, colour: Colour, position: PositionAlpha) -> None:
        self.type: PieceType = type
        self.colour: Colour = colour
        self.position: Position = Position(position)

    @dispatch(PieceType, Colour, tuple)
    def __init__(self, type: PieceType, colour: Colour, position: tuple) -> None:
        self.type: PieceType = type
        self.colour: Colour = colour
        self.position: Position = Position(position)

    def __str__(self):
        return f"Piece('{self.type}', '{self.colour}', '{self.position}')"


class Board(ChessBoard):
    # @dispatch(dict)
    # def __init__(self, piece_values: dict):
    #     self.piece_values: dict = piece_values

    def retrieve_piece_values(self, piece_values: dict[PieceType, int]):
        self.piece_values = piece_values

    def get_pieces(self, piece: PieceType=NONE, colour: Colour=NONE) -> list[Piece]:
        """
        >>> board = Board()
        >>> board.get_pieces()
        [... every piece on the board ...]
        >>> board.get_pieces(QUEEN)
        [Piece('q', 'w', 'd1'), Piece('q', 'b', 'd8')]
        >>> board.get_pieces(QUEEN, WHITE)
        [Piece('q', 'w', 'd1')]
        >>> board.get_pieces(QUEEN, BLACK)
        [Piece('q', 'b', 'd8')]
        >>> board.get_pieces(ROOK, WHITE)
        [Piece('r', 'w', 'a1'), Piece('r', 'w', 'h1')]
        """

        pieces = [PIECES.index(piece)]
        colours = [COLOURS.index(colour)]
        if piece == NONE:
            pieces = PIECE_TYPES
        if colour == NONE:
            colours = [False, True]
        
        result = []

        for colour in colours:
            for piece in pieces:
                piece_type = PIECES[piece]
                locations = self.pieces(piece, colour)
                for square in locations:
                    new_piece = Piece(piece_type, COLOURS[colour], Position(square))
                    result.append(new_piece)

        return result

    def get_value(self, pieces: list[Piece]):
        total_value = 0
        for piece in pieces:
            piece_value = self.piece_values[piece.type]
            total_value += piece_value
        return total_value

    def piece_attacks(piece: Piece) -> list[Piece] | None:
        """
        """

    def position_attacks(position: Position) -> list[Piece] | None:
        """
        CODE IS INVALID
        >>> board = Board()
        >>> board.get_pieces(board, WHITE, 'a1')
        []
        >>> board.get_pieces(board, WHITE, 'd4')
        None                                            # no piece at d4
        >>> board.move(board, WHITE, 'd2d3')            # not a real function
        >>> board.move(board, WHITE, 'c1h6')
        >>> board.get_pieces(board, WHITE, 'h6')
        ['g7']

        >>> board.get_pieces(board, WHITE, 'd6', QUEEN)
        ['c7', 'd7', 'e7']
        >>> board.get_pieces(board, WHITE, 'd6', KNIGHT)
        ['b7', 'c8', 'e8', 'f7']
        """
        pass

