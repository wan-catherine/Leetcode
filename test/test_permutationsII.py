from unittest import TestCase
from problems.PermutationsII import Solution

class TestSolution(TestCase):
    def test_permuteUnique(self):
        solution = Solution()
        res = solution.permuteUnique([1,1,2])
        l = [
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
        self.assertEqual(len(l), len(res))
        self.assertTrue(l[1] in res)

    def test_permuteUnique_copy(self):
        solution = Solution()
        res = solution.permuteUnique([2,2,1,1])
        l = [[1,1,2,2],[1,2,1,2],[1,2,2,1],[2,1,1,2],[2,1,2,1],[2,2,1,1]]
        self.assertEqual(len(l), len(res))
