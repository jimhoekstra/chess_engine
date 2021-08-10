from chess_app.src.legal_moves import LegalMoves
from chess_engine.src.position_evaluator import PositionEvaluator
from chess_engine.src.utils import get_other_player
import random


class ChessEngine:

    def __init__(self, player, chessboard_state, base_evaluation=None):
        self.player = player
        self.chessboard_state = chessboard_state

        if base_evaluation is None:
            self.base_evaluation = PositionEvaluator(player, self.chessboard_state, None).get_score()
        else:
            self.base_evaluation = base_evaluation

    def is_checkmate(self, all_legal_moves):
        return len(all_legal_moves) == 0

    def get_best_move(self, depth=1):
        all_legal_moves = LegalMoves(self.player, self.chessboard_state.get_state()).get_all_legal_moves()
        
        move_evaluations = []
        for move in all_legal_moves:
            new_chessboard_state = self.chessboard_state.make_move(move)

            best_response_evaluation = None

            if depth > 1:
                new_move_collector = ChessEngine(get_other_player(self.player), new_chessboard_state, base_evaluation=self.base_evaluation)
                best_response_move, best_response_evaluation = new_move_collector.get_best_move(depth=depth-1)

            new_evaluation = PositionEvaluator(self.player, new_chessboard_state, best_response_evaluation).get_score()

            evaluation_difference = new_evaluation - self.base_evaluation
            move_evaluations.append({'move': move, 'evaluation': evaluation_difference})
        
        shuffled_move_evaluations = random.sample(move_evaluations, k=len(move_evaluations))
        sorted_moves = sorted(shuffled_move_evaluations, key=lambda move: move['evaluation'], reverse=True)

        if depth == 2:
            for move_evaluation in move_evaluations:
                print(move_evaluation['move'].old, move_evaluation['move'].new, move_evaluation['evaluation'])
        
        return sorted_moves[0]['move'], sorted_moves[0]['evaluation']
