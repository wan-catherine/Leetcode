from unittest import TestCase
from problems.Combinations import Solution

class TestSolution(TestCase):
    def test_combine(self):
        solution = Solution()
        res = solution.combine(4, 2)
        expected = [
            [1, 2],
            [1, 3],
            [1, 4],
            [2, 3],
  [2,4],
  [3,4]


]
        self.assertEqual(res, expected)
