from unittest import TestCase
from problems.N1048_Longest_String_Chain import Solution

class TestSolution(TestCase):
    def test_longestStrChain(self):
        words = ["a","b","ba","bca","bda","bdca"]
        self.assertEqual(4, Solution().longestStrChain(words))

    def test_longestStrChain_1(self):
        words = ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]
        self.assertEqual(7, Solution().longestStrChain(words))
