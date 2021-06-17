from unittest import TestCase
from problems.N483_Smallest_Good_Base import Solution

class TestSolution(TestCase):
    def test_smallest_good_base(self):
        self.assertEqual("3", Solution().smallestGoodBase("13"))

    def test_smallest_good_base_1(self):
        self.assertEqual("8", Solution().smallestGoodBase("4681"))

