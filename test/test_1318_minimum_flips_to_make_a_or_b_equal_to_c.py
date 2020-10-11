from unittest import TestCase
from problems.N1318_Minimum_Flips_To_Make_A_Or_B_Equal_To_C import Solution

class TestSolution(TestCase):
    def test_minFlips(self):
        self.assertEqual(3, Solution().minFlips(2,6,5))

    def test_minFlips_1(self):
        self.assertEqual(1, Solution().minFlips(4,2,7))

    def test_minFlips_2(self):
        self.assertEqual(0, Solution().minFlips(1,2,3))

