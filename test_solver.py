
import unittest
from solver import GOAL, solve_puzzle, manhattan_distance, is_solvable, get_neighbors


class TestSolver(unittest.TestCase):

    def test_solved_board(self):
        result = solve_puzzle(GOAL)
        self.assertEqual(result, [list(GOAL)])

    def test_one_move(self):
        board = [1, 2, 3, 4, 5, 6, 7, 0, 8]
        result = solve_puzzle(board)
        self.assertEqual(len(result) - 1, 1)

    def test_two_moves(self):
        board = [1, 2, 3, 4, 5, 6, 0, 7, 8]
        result = solve_puzzle(board)
        self.assertEqual(len(result) - 1, 2)

    def test_unsolvable_board(self):
        board = [1, 2, 3, 4, 5, 6, 8, 7, 0]
        self.assertFalse(is_solvable(board))
        self.assertEqual(solve_puzzle(board), [])

    def test_distance(self):
        self.assertEqual(manhattan_distance(GOAL), 0)

    def test_neighbors(self):
        self.assertEqual(len(get_neighbors(GOAL)), 2)


if __name__ == "__main__":
    unittest.main()
