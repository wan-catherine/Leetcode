from unittest import TestCase
from problems.N831_Masking_Personal_Information import Solution

class TestSolution(TestCase):
    def test_maskPII(self):
        self.assertEqual("l*****e@leetcode.com", Solution().maskPII("LeetCode@LeetCode.com"))

    def test_maskPII_1(self):
        self.assertEqual("a*****b@qq.com", Solution().maskPII("AB@qq.com"))

    def test_maskPII_2(self):
        self.assertEqual("***-***-7890", Solution().maskPII("1(234)567-890"))

    def test_maskPII_3(self):
        self.assertEqual("+**-***-***-5678", Solution().maskPII("86-(10)12345678"))
