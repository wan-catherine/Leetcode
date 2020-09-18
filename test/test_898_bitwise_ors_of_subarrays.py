from unittest import TestCase
from problems.N898_Bitwise_Ors_Of_Subarrays import Solution

class TestSolution(TestCase):
    def test_subarrayBitwiseORs(self):
        self.assertEqual(1, Solution().subarrayBitwiseORs([0]))

    def test_subarrayBitwiseORs_1(self):
        self.assertEqual(3, Solution().subarrayBitwiseORs([1,1,2]))

    def test_subarrayBitwiseORs_2(self):
        self.assertEqual(6, Solution().subarrayBitwiseORs([1,2,4]))
