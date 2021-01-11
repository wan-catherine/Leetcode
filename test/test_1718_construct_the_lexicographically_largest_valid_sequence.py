from unittest import TestCase
from problems.N1718_Construct_The_Lexicographically_Largest_Valid_Sequence import Solution

class TestSolution(TestCase):
    def test_constructDistancedSequence(self):
        self.assertListEqual([3,1,2,3,2], Solution().constructDistancedSequence(3))

    def test_constructDistancedSequence_1(self):
        self.assertListEqual([5,3,1,4,3,5,2,4,2], Solution().constructDistancedSequence(5))

    def test_constructDistancedSequence_2(self):
        self.assertListEqual([6,4,2,5,2,4,6,3,5,1,3], Solution().constructDistancedSequence(6))
