from unittest import TestCase
from problems.N2338_Count_The_Number_Of_Ideal_Arrays import Solution

class TestSolution(TestCase):
    def test_ideal_arrays(self):
        self.assertEqual(10, Solution().idealArrays(n = 2, maxValue = 5))

    def test_ideal_arrays_1(self):
        self.assertEqual(11, Solution().idealArrays(n = 5, maxValue = 3))

    def test_ideal_arrays_2(self):
        self.assertEqual(1998089, Solution().idealArrays(9767, 9557))
