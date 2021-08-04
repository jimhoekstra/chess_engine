from chess_engine.src.position_evaluator import PositionEvaluator
import random


class MoveCollector:

    def __init__(self, player, chessboard_state, moves):
        self.player = player
        self.moves = moves
        self.chessboard_state = chessboard_state
        self.current_evaluation = PositionEvaluator(player, chessboard_state).get_score()
        self.move_evaluations = []

    def evaluate_moves(self):
        self.move_evaluations = []

        for move in self.moves:
            new_chessboard_state = self.chessboard_state.make_move(move)
            new_evaluation = PositionEvaluator(self.player, new_chessboard_state).get_score()
            evaluation_difference = new_evaluation - self.current_evaluation
            self.move_evaluations.append({'move': move, 'evaluation': evaluation_difference})

    def get_best_move(self):
        self.evaluate_moves()
        shuffled_move_evaluations = random.sample(self.move_evaluations, k=len(self.move_evaluations))
        sorted_moves = sorted(shuffled_move_evaluations, key=lambda move: move['evaluation'], reverse=True)
        return sorted_moves[0]['move']
