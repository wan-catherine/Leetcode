from unittest import TestCase
from problems.FindDifference import Solution

class TestSolution(TestCase):
    def test_findTheDifference(self):
        soluton = Solution()
        res = soluton.findTheDifference("abcd", "abcde")
        self.assertEqual(res, 'e')

    def test_findTheDifference_one(self):
        soluton = Solution()
        res = soluton.findTheDifference("abcd", "abcbd")
        self.assertEqual(res, 'b')