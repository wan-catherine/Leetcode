from unittest import TestCase
from problems.N2983_Palindrome_Rearrangement_Queries import Solution

class TestSolution(TestCase):
    def test_can_make_palindrome_queries(self):
        self.assertListEqual([True,True], Solution().canMakePalindromeQueries(s = "abcabc", queries = [[1,1,3,5],[0,2,5,5]]))

    def test_can_make_palindrome_queries_1(self):
        self.assertListEqual([False], Solution().canMakePalindromeQueries(s = "abbcdecbba", queries = [[0,2,7,9]]))

    def test_can_make_palindrome_queries_2(self):
        self.assertListEqual([True], Solution().canMakePalindromeQueries(s = "acbcab", queries = [[1,2,4,5]]))

    def test_can_make_palindrome_queries_3(self):
        self.assertListEqual([True], Solution().canMakePalindromeQueries(s = "cababc", queries = [[1,2,3,4]]))

    def test_can_make_palindrome_queries_4(self):
        self.assertListEqual([True], Solution().canMakePalindromeQueries(s = "ckwbnmqmtzbixrrkixbtbqzmnwmc", queries = [[1,9,15,24]]))
