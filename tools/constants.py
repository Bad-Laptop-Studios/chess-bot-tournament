PieceType = str # eg. 'k'
KING   = 'k'
QUEEN  = 'q'
ROOK   = 'r'
BISHOP = 'b'
KNIGHT = 'n'
PAWN   = 'p'
NONE   = '-'

PIECES = [NONE, PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING]
PIECE_TYPES = [1, 2, 3, 4, 5, 6]

Colour = str    # eg. 'w'
WHITE = 'W'
BLACK = 'B'
NONE = '-' # (duplicate) is this improper??

COLOURS = [BLACK, WHITE, NONE] # BLACK = 0 = False, WHITE = 1 = TRUE


PositionAlpha = str                 # eg. 'a1'
PositionVector = tuple[int, int]    # eg. (1, 1)

INFINITY = 1e9