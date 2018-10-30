from unittest import TestCase
from problems.PascalTriangle import Solution

class TestSolution(TestCase):
    def test_generate(self):
        solution = Solution()
        res = solution.generate(5)
        expected = [
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
        self.assertEqual(res, expected)
