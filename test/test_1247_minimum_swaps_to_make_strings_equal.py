from unittest import TestCase
from problems.N1247_Minimum_Swaps_To_Make_Strings_Equal import Solution

class TestSolution(TestCase):
    def test_minimumSwap(self):
        self.assertEqual(1, Solution().minimumSwap('xx', 'yy'))

    def test_minimumSwap_1(self):
        self.assertEqual(2, Solution().minimumSwap('xy', 'yx'))

    def test_minimumSwap_2(self):
        self.assertEqual(-1, Solution().minimumSwap('xx', 'xy'))

    def test_minimumSwap_3(self):
        self.assertEqual(4, Solution().minimumSwap('xxyyxyxyxx', 'xyyxyxxxyx'))

