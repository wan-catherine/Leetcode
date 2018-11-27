from unittest import TestCase
from problems.NumberOfOneBits import Solution

class TestSolution(TestCase):
    def test_hammingWeight(self):
        solution = Solution()
        res = solution.hammingWeight(11)
        self.assertEqual(3, res)


    def test_hammingWeight_one(self):
        solution = Solution()
        res = solution.hammingWeight(128)
        self.assertEqual(1, res)