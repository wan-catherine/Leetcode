from unittest import TestCase
from problems.N2354_Number_Of_Excellent_Pairs import Solution

class TestSolution(TestCase):
    def test_count_excellent_pairs(self):
        self.assertEqual(5, Solution().countExcellentPairs(nums = [1,2,3,1], k = 3))

    def test_count_excellent_pairs_1(self):
        self.assertEqual(0, Solution().countExcellentPairs(nums = [5,1,1], k = 10))

    def test_count_excellent_pairs_2(self):
        self.assertEqual(12, Solution().countExcellentPairs([1,2,3,1,536870911], 3))

    def test_count_excellent_pairs_3(self):
        self.assertEqual(81, Solution().countExcellentPairs([1,2,4,8,16,32,64,128,256], 2))
