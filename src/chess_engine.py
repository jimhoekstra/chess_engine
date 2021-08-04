from chess_app.src.move import Move
from chess_app.src.legal_moves import LegalMoves

from chess_engine.src.chessboard_state import ChessboardState
from chess_engine.src.move_collector import MoveCollector

import random


class ChessEngine:

    def __init__(self, move_data):
        self.player = move_data['player']
        self.move = move_data['move']
        self.chessboard_state = move_data['chessboardState']
        
    def get_random_move(self):
        all_legal_moves = LegalMoves(self.player, self.chessboard_state).get_all_legal_moves()
        if self.is_checkmate(all_legal_moves):
            return None, True
        
        random_move = random.choice(all_legal_moves)
        return random_move, False

    def get_best_move(self):
        chessboard_state = ChessboardState(self.chessboard_state)
        all_legal_moves = LegalMoves(self.player, self.chessboard_state).get_all_legal_moves()
        if self.is_checkmate(all_legal_moves):
            return None, True

        move_collector = MoveCollector(self.player, chessboard_state, all_legal_moves)
        return move_collector.get_best_move(), False

    def is_checkmate(self, all_legal_moves):
        return len(all_legal_moves) == 0
