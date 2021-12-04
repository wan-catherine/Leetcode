from unittest import TestCase
from problems.N2064_Minimized_Maximum_Of_Products_Distributed_To_Any_Store import Solution

class TestSolution(TestCase):
    def test_minimized_maximum(self):
        self.assertEqual(3, Solution().minimizedMaximum(n = 6, quantities = [11,6]))

    def test_minimized_maximum_1(self):
        self.assertEqual(5, Solution().minimizedMaximum(n = 7, quantities = [15,10,10]))

    def test_minimized_maximum_2(self):
        self.assertEqual(100000, Solution().minimizedMaximum(n = 1, quantities = [100000]))

    def test_minimized_maximum_3(self):
        self.assertEqual(13, Solution().minimizedMaximum(22, [25,11,29,6,24,4,29,18,6,13,25,30]))

    def test_minimized_maximum_4(self):
        self.assertEqual(1, Solution().minimizedMaximum(100000, [1]))
