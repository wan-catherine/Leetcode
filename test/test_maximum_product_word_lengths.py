from unittest import TestCase
from problems.MaximumProductWordLengths import Solution

class TestSolution(TestCase):
    def test_maxProduct(self):
        solution = Solution()
        res = solution.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"])
        self.assertEqual(res, 16)

    def test_maxProduct_one(self):
        solution = Solution()
        res = solution.maxProduct(["a","ab","abc","d","cd","bcd","abcd"])
        self.assertEqual(res, 4)

    def test_maxProduct_two(self):
        solution = Solution()
        res = solution.maxProduct(["a","aa","aaa","aaaa"])
        self.assertEqual(res, 0)

