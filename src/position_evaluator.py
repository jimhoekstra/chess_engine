from chess_engine.src.utils import get_other_player


PIECE_VALUES = {'pawn': 1, 'knight': 3, 'bishop': 3, 'rook': 5, 'queen': 9, 'king': 0}


class PositionEvaluator:

    def __init__(self, player, chessboard_state, best_response):
        self.player = player
        self.chessboard_state = chessboard_state
        self.best_response = best_response

    def get_score(self):
        if self.best_response is not None:
            return -self.best_response
        
        score = self.chessboard_state.get_scores(PIECE_VALUES)
        return score[self.player] - score[get_other_player(self.player)]
