from unittest import TestCase
from problems.N1239_Maximum_Length_Of_A_Concatenated_String_With_Unique_Characters import Solution

class TestSolution(TestCase):
    def test_maxLength(self):
        self.assertEqual(4, Solution().maxLength(["un","iq","ue"]))

    def test_maxLength_1(self):
        self.assertEqual(6, Solution().maxLength(["cha","r","act","ers"]))

    def test_maxLength_2(self):
        self.assertEqual(26, Solution().maxLength(["abcdefghijklmnopqrstuvwxyz"]))

    def test_maxLength_3(self):
        self.assertEqual(6, Solution().maxLength(["a", "abc", "d", "de", "def"]))

    def test_maxLength_4(self):
        self.assertEqual(16, Solution().maxLength(["jnfbyktlrqumowxd","mvhgcpxnjzrdei"]))
