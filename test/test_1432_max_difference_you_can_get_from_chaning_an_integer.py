from unittest import TestCase
from problems.N1432_Max_Difference_You_Can_Get_From_Changing_An_Integer import Solution

class TestSolution(TestCase):
    def test_maxDiff(self):
        self.assertEqual(888, Solution().maxDiff(555))

    def test_maxDiff_1(self):
        self.assertEqual(8, Solution().maxDiff(9))

    def test_maxDiff_2(self):
        self.assertEqual(820000, Solution().maxDiff(123456))

    def test_maxDiff_3(self):
        self.assertEqual(80000, Solution().maxDiff(10000))

    def test_maxDiff_4(self):
        self.assertEqual(8700, Solution().maxDiff(9288))

    def test_maxDiff_5(self):
        self.assertEqual(888, Solution().maxDiff(111))

    def test_maxDiff_6(self):
        self.assertEqual(8808050, Solution().maxDiff(1101057))
