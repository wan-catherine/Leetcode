from unittest import TestCase
from problems.N2779_Maximum_Beauty_Of_An_Array_After_Applying_Operation import Solution

class TestSolution(TestCase):
    def test_maximum_beauty(self):
        self.assertEquals(3, Solution().maximumBeauty(nums = [4,6,1,2], k = 2))

    def test_maximum_beauty_1(self):
        self.assertEquals(4, Solution().maximumBeauty(nums = [1,1,1,1], k = 10))
