from unittest import TestCase
from problems.N1559_Detect_Cycles_In_2d_Grid import Solution

class TestSolution(TestCase):
    def test_containsCycle(self):
        grid = [["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]]
        self.assertTrue(Solution().containsCycle(grid))

    def test_containsCycle_1(self):
        grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
        self.assertTrue(Solution().containsCycle(grid))

    def test_containsCycle_2(self):
        grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
        self.assertFalse(Solution().containsCycle(grid))
