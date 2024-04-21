from unittest import TestCase
from problems.N2563_Count_The_Number_Of_Fair_Pairs import Solution

class TestSolution(TestCase):
    def test_count_fair_pairs(self):
        self.assertEquals(6, Solution().countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6))

    def test_count_fair_pairs_1(self):
        self.assertEquals(1, Solution().countFairPairs(nums = [1,7,9,2,5], lower = 11, upper = 11))

    def test_count_fair_pairs_2(self):
        self.assertEquals(15, Solution().countFairPairs(nums = [0,0,0,0,0,0], lower = 0, upper = 0))

