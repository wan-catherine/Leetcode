from unittest import TestCase
from problems.N2612_Minimum_Reverse_Operations import Solution

class TestSolution(TestCase):
    def test_min_reverse_operations(self):
        self.assertListEqual([0,-1,-1,1], Solution().minReverseOperations(n = 4, p = 0, banned = [1,2], k = 4))

    def test_min_reverse_operations_1(self):
        self.assertListEqual([0,-1,-1,-1,-1], Solution().minReverseOperations(n = 5, p = 0, banned = [2,4], k = 3))

    def test_min_reverse_operations_2(self):
        self.assertListEqual([-1,-1,0,-1], Solution().minReverseOperations(n = 4, p = 2, banned = [0,1,3], k = 1))

    def test_min_reverse_operations_3(self):
        self.assertListEqual([0,-1,-1,1], Solution().minReverseOperations(n = 4, p = 0, banned = [], k = 4))
