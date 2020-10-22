from unittest import TestCase
from problems.N135_Candy import Solution

class TestSolution(TestCase):
    def test_candy(self):
        self.assertEqual(5, Solution().candy([1,0,2]))

    def test_candy_1(self):
        self.assertEqual(4, Solution().candy([1,2,2]))

    def test_candy_2(self):
        self.assertEqual(7, Solution().candy([1,3,2,2,1]))
