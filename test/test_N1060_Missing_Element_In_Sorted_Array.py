from unittest import TestCase
from problems.N1060_Missing_Element_In_Sorted_Array import Solution

class TestSolution(TestCase):
    def test_missing_element(self):
        self.assertEqual(5, Solution().missingElement(nums = [4,7,9,10], k = 1))

    def test_missing_element_1(self):
        self.assertEqual(8, Solution().missingElement(nums = [4,7,9,10], k = 3))

    def test_missing_element_2(self):
        self.assertEqual(6, Solution().missingElement(nums = [1,2,4], k = 3))
