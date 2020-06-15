from unittest import TestCase
from .N5437_Least_Number_Of_Unique_Integers_After_K_Removals import Solution

class TestSolution(TestCase):
    def test_findLeastNumOfUniqueInts(self):
        arr = [5, 5, 4]
        k = 1
        self.assertEqual(1, Solution().findLeastNumOfUniqueInts(arr, k))

    def test_findLeastNumOfUniqueInts_1(self):
        arr = [4, 3, 1, 1, 3, 3, 2]
        k = 3
        self.assertEqual(2, Solution().findLeastNumOfUniqueInts(arr, k))

    def test_findLeastNumOfUniqueInts_2(self):
        arr = [2,4,1,8,3,5,1,3]
        k = 3
        self.assertEqual(3, Solution().findLeastNumOfUniqueInts(arr, k))

    def test_findLeastNumOfUniqueInts_3(self):
        arr = [2,1,1,3,3,3]
        k = 3
        self.assertEqual(1, Solution().findLeastNumOfUniqueInts(arr, k))

