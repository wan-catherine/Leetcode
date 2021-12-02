from unittest import TestCase
from problems.N2081_Sum_Of_K_Mirror_Numbers import Solution

class TestSolution(TestCase):
    def test_k_mirror(self):
        self.assertEqual(25, Solution().kMirror(k = 2, n = 5))

    def test_k_mirror_1(self):
        self.assertEqual(499, Solution().kMirror(k = 3, n = 7))

    def test_k_mirror_2(self):
        self.assertEqual(20379000, Solution().kMirror(k = 7, n = 17))
