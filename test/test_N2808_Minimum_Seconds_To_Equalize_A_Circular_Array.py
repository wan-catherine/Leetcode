from unittest import TestCase
from problems.N2808_Minimum_Seconds_To_Equalize_A_Circular_Array import Solution

class TestSolution(TestCase):
    def test_minimum_seconds(self):
        self.assertEquals(1, Solution().minimumSeconds([1,2,1,2]))

    def test_minimum_seconds_1(self):
        self.assertEquals(2, Solution().minimumSeconds([2,1,3,3,2]))

    def test_minimum_seconds_2(self):
        self.assertEquals(0, Solution().minimumSeconds([5,5,5,5]))

    def test_minimum_seconds_3(self):
        self.assertEquals(1, Solution().minimumSeconds([4,18]))

    def test_minimum_seconds_4(self):
        self.assertEquals(1, Solution().minimumSeconds([8,13,3,3]))

    def test_minimum_seconds_5(self):
        self.assertEquals(2, Solution().minimumSeconds([11,15,15,4,12,18]))

    def test_minimum_seconds_6(self):
        self.assertEquals(1, Solution().minimumSeconds([11,4,10]))