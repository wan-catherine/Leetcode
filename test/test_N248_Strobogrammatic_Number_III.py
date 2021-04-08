from unittest import TestCase
from problems.N248_Strobogrammatic_Number_III import Solution

class TestSolution(TestCase):
    def test_strobogrammatic_in_range(self):
        self.assertEqual(3, Solution().strobogrammaticInRange(low = "50", high = "100"))

    def test_strobogrammatic_in_range_1(self):
        self.assertEqual(1, Solution().strobogrammaticInRange(low = "0", high = "0"))
