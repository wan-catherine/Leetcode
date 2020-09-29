from unittest import TestCase
from problems.N880_Decoded_String_At_Index import Solution

class TestSolution(TestCase):
    def test_decodeAtIndex(self):
        self.assertEqual('o', Solution().decodeAtIndex(S = "leet2code3", K = 10))

    def test_decodeAtIndex_1(self):
        self.assertEqual('h', Solution().decodeAtIndex(S = "ha22", K = 5))

    def test_decodeAtIndex_2(self):
        self.assertEqual('a', Solution().decodeAtIndex(S = "a2345678999999999999999", K = 1))

    def test_decodeAtIndex_3(self):
        self.assertEqual('c', Solution().decodeAtIndex("a2b3c4d5e6f7g8h9", 10))

    def test_decodeAtIndex_4(self):
        self.assertEqual('z', Solution().decodeAtIndex("vzpp636m8y", 2920))

    def test_decodeAtIndex_5(self):
        self.assertEqual('a', Solution().decodeAtIndex("a23", 6))

