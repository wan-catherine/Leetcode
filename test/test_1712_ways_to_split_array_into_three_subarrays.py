from unittest import TestCase
from problems.N1712_Ways_To_Split_Array_Into_Three_Subarrays import Solution

class TestSolution(TestCase):
    def test_waysToSplit(self):
        self.assertEqual(1, Solution().waysToSplit([1,1,1]))

    def test_waysToSplit_1(self):
        self.assertEqual(3, Solution().waysToSplit([1,2,2,2,5,0]))

    def test_waysToSplit_2(self):
        self.assertEqual(1, Solution().waysToSplit([0,3,3]))

    def test_waysToSplit_3(self):
        self.assertEqual(6, Solution().waysToSplit([0,0,0,0,0]))

