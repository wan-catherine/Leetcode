from unittest import TestCase
from problems.N1338_Reduce_Array_Size_To_The_Half import Solution

class TestSolution(TestCase):
    def test_minSetSize(self):
        arr = [3,3,3,3,5,5,5,2,2,7]
        self.assertEqual(2, Solution().minSetSize(arr))

    def test_minSetSize_1(self):
        arr = [7,7,7,7,7,7]
        self.assertEqual(1, Solution().minSetSize(arr))

    def test_minSetSize_2(self):
        arr =  [1,9]
        self.assertEqual(1, Solution().minSetSize(arr))

    def test_minSetSize_1(self):
        arr = [1000,1000,3,7]
        self.assertEqual(1, Solution().minSetSize(arr))

    def test_minSetSize_1(self):
        arr =  [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(5, Solution().minSetSize(arr))
