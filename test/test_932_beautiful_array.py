from unittest import TestCase
from problems.N932_Beautiful_Array import Solution

class TestSolution(TestCase):
    def test_beautifulArray(self):
        self.assertListEqual([2,1,4,3], Solution().beautifulArray(4))

    def test_beautifulArray_1(self):
        self.assertListEqual([3,1,2,5,4], Solution().beautifulArray(5))
