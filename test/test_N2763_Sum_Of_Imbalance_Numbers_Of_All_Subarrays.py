from unittest import TestCase
from problems.N2763_Sum_Of_Imbalance_Numbers_Of_All_Subarrays import Solution

class TestSolution(TestCase):
    def test_sum_imbalance_numbers(self):
        self.assertEquals(3, Solution().sumImbalanceNumbers([2,3,1,4]))

    def test_sum_imbalance_numbers_1(self):
        self.assertEquals(8, Solution().sumImbalanceNumbers([1,3,3,3,5]))
