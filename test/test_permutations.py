from unittest import TestCase
from problems.Permutations import Solution

class TestSolution(TestCase):
    def test_permute(self):
        solution = Solution()
        res = solution.permute([1,2,3])
        l=[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
        self.assertTrue(l[0] in res)
        self.assertEqual(len(l), len(res))

    def test_permute(self):
        solution = Solution()
        res = solution.permute([1])
        self.assertEqual([[1]],res)
