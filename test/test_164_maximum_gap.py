from unittest import TestCase
from problems.N164_Maximum_Gap import Solution

class TestSolution(TestCase):
    def test_maximumGap(self):
        self.assertEqual(3, Solution().maximumGap([3,6,9,1]))

    def test_maximumGap_1(self):
        self.assertEqual(0, Solution().maximumGap([10]))

    def test_maximumGap_2(self):
        self.assertEqual(97, Solution().maximumGap([1,3,100]))
