from unittest import TestCase
from problems.N2611_Mice_And_Cheese import Solution

class TestSolution(TestCase):
    def test_mice_and_cheese(self):
        self.assertEqual(15, Solution().miceAndCheese(reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2))

    def test_mice_and_cheese_1(self):
        self.assertEqual(2, Solution().miceAndCheese(reward1 = [1,1], reward2 = [1,1], k = 2))
