from unittest import TestCase
from problems.N1073_Adding_Two_Negabinary_Numbers import Solution

class TestSolution(TestCase):
    def test_addNegabinary(self):
        self.assertListEqual([1,0,0,0,0], Solution().addNegabinary(arr1 = [1,1,1,1,1], arr2 = [1,0,1]))

    def test_addNegabinary_1(self):
        self.assertListEqual([0], Solution().addNegabinary([0], [0]))

    def test_addNegabinary_2(self):
        self.assertListEqual([1], Solution().addNegabinary([0], [1]))
