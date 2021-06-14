from unittest import TestCase
from problems.N1449_Form_Largest_Integer_With_Digits_That_Add_Up_To_Target import Solution

class TestSolution(TestCase):
    def test_largest_number(self):
        self.assertEqual("7772", Solution().largestNumber(cost = [4,3,2,5,6,7,2,5,5], target = 9))

    def test_largest_number_1(self):
        self.assertEqual("85", Solution().largestNumber(cost = [7,6,5,5,5,6,8,7,8], target = 12))

    def test_largest_number_2(self):
        self.assertEqual("0", Solution().largestNumber(cost = [2,4,6,2,4,6,4,4,4], target = 5))

    def test_largest_number_3(self):
        self.assertEqual("32211", Solution().largestNumber(cost = [6,10,15,40,40,40,40,40,40], target = 47))
