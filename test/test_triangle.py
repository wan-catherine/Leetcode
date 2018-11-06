from unittest import TestCase
from problems.Triangle import Solution

class TestSolution(TestCase):
    def test_minimumTotal(self):
        solution = Solution()
        input = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
        res = solution.minimumTotal(input)
        self.assertEqual(11, res)
