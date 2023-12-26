from unittest import TestCase
from problems.N2945_Find_Maximum_Non_Decreasing_Array_Length import Solution

class TestSolution(TestCase):
    def test_find_maximum_length(self):
        self.assertEquals(1, Solution().findMaximumLength([5,2,2]))

    def test_find_maximum_length_1(self):
        self.assertEquals(4, Solution().findMaximumLength([1,2,3,4]))

    def test_find_maximum_length_2(self):
        self.assertEquals(3, Solution().findMaximumLength([4,3,2,6]))

    def test_find_maximum_length_3(self):
        self.assertEquals(4, Solution().findMaximumLength([336,78,256,976,976,764,370,46]))
