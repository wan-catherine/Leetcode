from unittest import TestCase
from problems.N1675_Minimize_Deviation_In_Array import Solution

class TestSolution(TestCase):
    def test_minimumDeviation(self):
        self.assertEqual(1, Solution().minimumDeviation([1,2,3,4]))

    def test_minimumDeviation_1(self):
        self.assertEqual(3, Solution().minimumDeviation([4,1,5,20,3]))

    def test_minimumDeviation_2(self):
        self.assertEqual(3, Solution().minimumDeviation([2,10,8]))