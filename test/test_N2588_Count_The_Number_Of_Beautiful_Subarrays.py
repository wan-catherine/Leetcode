from unittest import TestCase
from problems.N2588_Count_The_Number_Of_Beautiful_Subarrays import Solution

class TestSolution(TestCase):
    def test_beautiful_subarrays(self):
        self.assertEqual(2, Solution().beautifulSubarrays([4,3,1,2,4]))

    def test_beautiful_subarrays_1(self):
        self.assertEqual(0, Solution().beautifulSubarrays([1,10,4]))
