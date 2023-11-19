from unittest import TestCase
from problems.N2866_Beautiful_Towers_II import Solution

class TestSolution(TestCase):
    def test_maximum_sum_of_heights(self):
        self.assertEquals(13, Solution().maximumSumOfHeights([5,3,4,1,1]))

    def test_maximum_sum_of_heights_1(self):
        self.assertEquals(22, Solution().maximumSumOfHeights([6,5,3,9,2,7]))

    def test_maximum_sum_of_heights_2(self):
        self.assertEquals(18, Solution().maximumSumOfHeights([3,2,5,5,2,3]))
