from unittest import TestCase
from problems.N896_Monotonic_Array import Solution

class TestSolution(TestCase):
    def test_isMonotonic(self):
        self.assertEqual(True, Solution().isMonotonic([1,2,2,3]))

    def test_isMonotonic_1(self):
        self.assertEqual(True, Solution().isMonotonic([6,5,4,4]))

    def test_isMonotonic_2(self):
        self.assertEqual(False, Solution().isMonotonic([1,3,2]))

    def test_isMonotonic_3(self):
        self.assertEqual(True, Solution().isMonotonic([1,2,4,5]))

    def test_isMonotonic_4(self):
        self.assertEqual(True, Solution().isMonotonic([1,1,1]))
