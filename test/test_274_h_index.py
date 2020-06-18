from unittest import TestCase
from problems.N274_H_Index import Solution

class TestSolution(TestCase):
    def test_hIndex(self):
        self.assertEqual(3, Solution().hIndex([3,0,6,1,5]))

    def test_hIndex_1(self):
        self.assertEqual(1, Solution().hIndex([1]))

    def test_hIndex_2(self):
        self.assertEqual(1, Solution().hIndex([0,1]))

