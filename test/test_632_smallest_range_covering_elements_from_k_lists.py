from unittest import TestCase
from problems.N632_Smallest_Range_Covering_Elements_From_K_Lists import Solution

class TestSolution(TestCase):
    def test_smallestRange(self):
        self.assertListEqual([20,24], Solution().smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))

    def test_smallestRange_1(self):
        self.assertListEqual([10,11], Solution().smallestRange([[10,10],[11,11]]))

    def test_smallestRange_2(self):
        self.assertListEqual([1,1], Solution().smallestRange([[1,2,3],[1,2,3],[1,2,3]]))

    def test_smallestRange_3(self):
        self.assertListEqual([10,11], Solution().smallestRange([[10],[11]]))

    def test_smallestRange_4(self):
        self.assertListEqual([1,7], Solution().smallestRange([[1],[2],[3],[4],[5],[6],[7]]))

    def test_smallestRange_5(self):
        self.assertListEqual([1,1], Solution().smallestRange([[-5,-4,-3,-2,-1,1],[1,2,3,4,5]]))
