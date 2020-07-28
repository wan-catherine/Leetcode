from unittest import TestCase
from problems.N554_Brick_Wall import Solution

class TestSolution(TestCase):
    def test_leastBricks(self):
        input =  [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]
        self.assertEqual(2, Solution().leastBricks(input))

    def test_leastBricks_1(self):
        input =  [[1],[1],[1]]
        self.assertEqual(3, Solution().leastBricks(input))
