from unittest import TestCase
from problems.N1760_Minimum_Limit_Of_Balls_In_A_Bag import Solution

class TestSolution(TestCase):
    def test_minimumSize(self):
        self.assertEqual(3, Solution().minimumSize([9], 2))

    def test_minimumSize_1(self):
        self.assertEqual(4, Solution().minimumSize([2,4,8,2], 4))

    def test_minimumSize_2(self):
        self.assertEqual(1, Solution().minimumSize([1], 1))
