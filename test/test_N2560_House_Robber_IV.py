from unittest import TestCase
from problems.N2560_House_Robber_IV import Solution

class TestSolution(TestCase):
    def test_min_capability(self):
        self.assertEquals(5, Solution().minCapability(nums = [2,3,5,9], k = 2))

    def test_min_capability_1(self):
        self.assertEquals(2, Solution().minCapability(nums = [2,7,9,3,1], k = 2))
