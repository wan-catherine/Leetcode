from unittest import TestCase
from problems.DecodeWays import Solution

class TestSolution(TestCase):
    def test_numDecodings(self):
        solution = Solution()
        res = solution.numDecodings("22")
        self.assertEqual(2, res)

    def test_numDecodings_one(self):
        solution = Solution()
        res = solution.numDecodings("226")
        self.assertEqual(3, res)

    def test_numDecodings_two(self):
        solution = Solution()
        res = solution.numDecodings("0")
        self.assertEqual(0, res)

    def test_numDecodings_three(self):
        solution = Solution()
        res = solution.numDecodings("10")
        self.assertEqual(1, res)

    def test_numDecodings_four(self):
        solution = Solution()
        res = solution.numDecodings("301")
        self.assertEqual(0, res)

    def test_numDecodings_five(self):
        solution = Solution()
        res = solution.numDecodings("17")
        self.assertEqual(2, res)

    def test_numDecodings_six(self):
        solution = Solution()
        res = solution.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")
        self.assertEqual(589824, res)

    def test_numDecodings_seven(self):
        solution = Solution()
        res = solution.numDecodings("2941")
        self.assertEqual(1, res)

    def test_numDecodings_eight(self):
        solution = Solution()
        res = solution.numDecodings("1")
        self.assertEqual(1, res)

    def test_numDecodings_night(self):
        solution = Solution()
        res = solution.numDecodings("101")
        self.assertEqual(1, res)

    def test_numDecodings_ten(self):
        solution = Solution()
        res = solution.numDecodings("110")
        self.assertEqual(1, res)

    def test_numDecodings_11(self):
        solution = Solution()
        res = solution.numDecodings("100")
        self.assertEqual(0, res)