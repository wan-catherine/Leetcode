from unittest import TestCase
from problems.N336_Palindrome_Pairs import Solution

class TestSolution(TestCase):
    def test_palindromePairs(self):
        self.assertListEqual([[0,1],[1,0],[3,2],[2,4]], Solution().palindromePairs(["abcd","dcba","lls","s","sssll"]))

    def test_palindromePairs_1(self):
        self.assertListEqual([[0,1],[1,0]], Solution().palindromePairs(["bat","tab","cat"]))

    def test_palindromePairs_2(self):
        self.assertListEqual([[0,1],[1,0]], Solution().palindromePairs(["a",""]))
