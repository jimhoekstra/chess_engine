from chess_app.src.legal_moves import LegalMoves
from chess_app.src.move import Move
import random


class ChessEngine:

    def __init__(self, move_data):
        self.player = move_data['player']
        self.move = move_data['move']
        self.chessboard_state = move_data['chessboardState']
        
    def get_random_move(self):
        all_legal_moves = LegalMoves(self.player, self.chessboard_state).get_all_legal_moves()
        if len(all_legal_moves) == 0:
            return None, True
        random_move = random.choice(all_legal_moves)
        return Move(random_move['piece'], random_move['old'], random_move['new']).as_dict(), False
