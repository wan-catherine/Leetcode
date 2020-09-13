from unittest import TestCase
from problems.N474_Ones_And_Zeroes import Solution

class TestSolution(TestCase):
    def test_findMaxForm(self):
        self.assertEqual(4, Solution().findMaxForm(strs = ["10","0001","111001","1","0"], m = 5, n = 3))

    def test_findMaxForm_1(self):
        self.assertEqual(2, Solution().findMaxForm(strs = ["10","0","1"], m = 1, n = 1))

    def test_findMaxForm_2(self):
        self.assertEqual(4, Solution().findMaxForm(["0","0","1","1"], 2, 2))

    def test_findMaxForm_3(self):
        self.assertEqual(3, Solution().findMaxForm(["10","0001","111001","1","0"], 3, 4))

    def test_findMaxForm_4(self):
        self.assertEqual(45, Solution().findMaxForm(["011","1","11","0","010","1","10","1","1","0","0","0","01111","011","11","00","11","10","1","0","0","0","0","101","001110","1","0","1","0","0","10","00100","0","10","1","1","1","011","11","11","10","10","0000","01","1","10","0"], 44, 39))
