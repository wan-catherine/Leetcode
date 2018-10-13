from unittest import TestCase
from problems.SubsetsII import Solution

class TestSolution(TestCase):
    def test_subsetsWithDup(self):
        solution = Solution()
        res = solution.subsetsWithDup([1,2,2])
        output = [
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
        self.assertEqual(sorted(output), sorted(res))
