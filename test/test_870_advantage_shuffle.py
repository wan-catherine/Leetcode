from unittest import TestCase
from problems.N870_Advantage_Shuffle import Solution

class TestSolution(TestCase):
    def test_advantageCount(self):
        A = [2, 7, 11, 15]
        B = [1, 10, 4, 11]
        self.assertListEqual([2,11,7,15], Solution().advantageCount(A, B))

    def test_advantageCount_1(self):
        A = [12, 24, 8, 32]
        B = [13, 25, 32, 11]
        self.assertListEqual([24,32,8,12], Solution().advantageCount(A, B))
