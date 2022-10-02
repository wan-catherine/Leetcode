from unittest import TestCase
from problems.N2430_Maximum_Deletions_On_A_String import Solution

class TestSolution(TestCase):
    def test_delete_string(self):
        self.assertEqual(2, Solution().deleteString("abcabcdabc"))
