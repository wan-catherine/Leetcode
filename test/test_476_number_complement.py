from unittest import TestCase
from problems.N476_Number_Complement import Solution

class TestSolution(TestCase):
    def test_findComplement(self):
        res = Solution().findComplement(5)
        self.assertEqual(2, res)

    def test_findComplement_1(self):
        res = Solution().findComplement(1)
        self.assertEqual(0, res)

    def test_findComplement_2(self):
        res = Solution().findComplement(11)
        self.assertEqual(4, res)
