from unittest import TestCase
from problems.Subsets import Solution

class TestSolution(TestCase):
    def test_subsets(self):
        solution = Solution()
        res = solution.subsets([1,2,3])
        expected = [
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
        self.assertEqual(sorted(res), sorted(expected))
