from unittest import TestCase
from problems.N2929_Distribute_Candies_Among_Children_II import Solution

class TestSolution(TestCase):
    def test_distribute_candies(self):
        self.assertEquals(3, Solution().distributeCandies(n = 5, limit = 2))

    def test_distribute_candies_1(self):
        self.assertEquals(10, Solution().distributeCandies(n = 3, limit = 3))

    def test_distribute_candies_1(self):
        self.assertEquals(10, Solution().distributeCandies(n = 3, limit = 3))

