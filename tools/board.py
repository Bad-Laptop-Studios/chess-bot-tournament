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
        self.row = int(file_rank[1])
        self.col = self.COLUMN_LOOKUP.index(file_rank[0]) + 1

        self.square = (self.row - 1) * 8 + (self.col - 1)

    @dispatch(int, int)
    def __init__(self, row: int, col: int):
        """3,5"""
        self.row = row
        self.col = col

        self.square = (row - 1) * 8 + (col - 1)

    @dispatch(int)
    def __init__(self, square: int):
        self.row = chess.square_rank(square) + 1
        self.col = chess.square_file(square) + 1

        self.square = square

    COLUMN_LOOKUP = "abcdefgh"

    def __str__(self):
        return self.get_alphanumeric()
    
    def get_alphanumeric(self) -> PositionAlpha:
        return chess.square_name(self.square)
    
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

    @dispatch(PieceType, Colour, int)
    def __init__(self, type: PieceType, colour: Colour, position: int) -> None:
        self.type: PieceType = type
        self.colour: Colour = colour
        self.position: Position = Position(position)

    def __str__(self):
        return f"Piece('{self.type}', '{self.colour}', '{self.position}')"


class Board(ChessBoard):
    # @dispatch(dict)
    # def __init__(self, piece_values: dict):
    #     self.piece_values: dict = piece_values

    PIECE_VALUES = {
        KING: 0,
        QUEEN: 9,
        ROOK: 5,
        BISHOP: 3,
        KNIGHT: 3,
        PAWN: 1
    }

    def get_pieces(self, piece: PieceType=NONE, colour: Colour=NONE) -> list[Piece]:
        """
        >>> board = Board()
        >>> board.get_pieces()
        [... every piece on the board ...]
        >>> board.get_pieces(my_colour)
        [... all of your pieces on the board ...]
        >>> board.get_pieces(QUEEN)
        [Piece('q', 'w', 'd1'), Piece('q', 'b', 'd8')]
        >>> board.get_pieces(QUEEN, WHITE)
        [Piece('q', 'w', 'd1')]
        >>> board.get_pieces(QUEEN, BLACK)
        [Piece('q', 'b', 'd8')]
        >>> board.get_pieces(ROOK, WHITE)
        [Piece('r', 'w', 'a1'), Piece('r', 'w', 'h1')]
        >>> board.get_pieces([QUEEN, ROOK], WHITE)
        [Piece('q', 'w', 'd1'), Piece('r', 'w', 'a1'), Piece('r', 'w', 'h1')]
        """

        # swap variables if a colour was provided as the first argument
        if WHITE in piece or BLACK in piece:
            piece, colour = colour, piece

        pieces = self.get_piece_list(piece)
        colours = self.get_colour_list(colour)
        
        piece_list = []

        for colour in colours:
            for piece in pieces:
                piece_type = PIECES[piece]
                locations = self.pieces(piece, colour)
                for square in locations:
                    new_piece = Piece(piece_type, COLOURS[colour], Position(square))
                    piece_list.append(new_piece)

        return piece_list
    
    def get_piece_list(self, piece):
        pieces = [PIECES.index(p) for p in piece]
        if piece == NONE:
            pieces = PIECE_TYPES
        return pieces
    
    def get_colour_list(self, colour):
        colours = [COLOURS.index(c) for c in colour]
        if colour == NONE:
            colours = [False, True]
        return colours

    def get_value(self, pieces: list[Piece], provided_piece_values: dict[Piece, int] = {}):
        """
        >>> board = Board()
        >>> pieces = board.get_pieces()
        >>> board.get_value(pieces)
        78                                          # total value of all pieces, initially
        >>> pawns = board.get_pieces(PAWN)
        >>> board.get_value(pawns)
        16                                          # total value of the initial 16 pawns
        >>> my_pieces = board.get_pieces(my_colour)
        >>> board.get_value(my_pieces)
        39                                          # total value of all your pieces, initially
        >>> my_pawns = board.get_pieces(PAWN, my_colour)
        >>> board.get_value(my_pawns)
        8                                           # total value of your initial 8 pawns
        >>> board.get_value(my_pawns, {PAWN:1.5})
        12.0                                        # total value of your initial 8 pawns if they were worth 1.5 points each
        >>> my_minor_pieces = board.get_pieces([KNIGHT, BISHOP], my_colour)
        >>> board.get_value(my_minor_pieces, {KNIGHT: 2.5, BISHOP: 4})
        13.0                                        # total value of your initial knights and bishops
                                                    # if your knights were worth 2.5 and bishops were worth 4
        """
        total_value = 0
        for piece in pieces:
            piece_value = provided_piece_values.get(piece.type, self.PIECE_VALUES[piece.type])
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

