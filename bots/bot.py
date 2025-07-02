from chess import Board as ChessBoard
from tools.constants import *
from tools.board import *

from typing import final


class Bot:
    """ Template for creating a bot. """
    @final
    def __init__(self, bot_id):
        """ 
        Initialise the bot and variables. DO NOT MODIFY.
        """
        # self.chess_board = None
        # self.colour = colour
        # self.board = Board
        self.bot_id = bot_id

        self.initialise()


    # @final
    # def set_board(self, board: Board) -> None:
    #     self.board = board


    def initialise(self):
        """ You may edit this method. """
        pass


    def heuristic(self, board: Board) -> float:
        """
        Evaluates the provided board state and returns the perceived evaluation score.
        A high number represents a more favourable board state for the bot.
        """
        raise NotImplementedError

    
    def provide_game_over_evaluations(self) -> dict[str, float]:
        return {
            "win": INFINITY,
            "draw": 0,
            "loss": -INFINITY
        }
    
    @final
    def get_positions(self, piece: Piece) -> list[Position]:
        return self.analyser.get_positions(self.board, self.colour, piece)
    
    @final
    def position_attacks(self, position: Position, piece: Piece=None) -> list[(Position, Piece)]:
        return self.analyser.position_attacks(self.board, self.colour, position, piece)