from unittest import TestCase
from problems.N421_Maximum_XOR_Of_Two_Numbers_In_An_Array import Solution

class TestSolution(TestCase):
    def test_findMaximumXOR(self):
        self.assertEqual(28, Solution().findMaximumXOR([3, 10, 5, 25, 2, 8]))

    def test_findMaximumXOR_1(self):
        self.assertEqual(13, Solution().findMaximumXOR([14,15,9,3,2]))