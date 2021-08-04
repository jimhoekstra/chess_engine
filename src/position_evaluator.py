PIECE_VALUES = {'pawn': 1, 'knight': 3, 'bishop': 3, 'rook': 5, 'queen': 9, 'king': 0}


class PositionEvaluator:

    def __init__(self, player, chessboard_state):
        self.player = player
        self.chessboard_state = chessboard_state

    def get_score(self):
        score = self.chessboard_state.get_scores(PIECE_VALUES)
        return score[self.player] - score[self.get_other_player()]

    def get_other_player(self):
        if self.player == 'white':
            return 'black'
        if self.player == 'black':
            return 'white'
