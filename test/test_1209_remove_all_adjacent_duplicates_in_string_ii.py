from unittest import TestCase
from problems.N1209_Remove_All_Adjacent_Duplicates_In_String_II import Solution

class TestSolution(TestCase):
    def test_removeDuplicates(self):
        self.assertEqual("abcd", Solution().removeDuplicates("abcd", 2))

    def test_removeDuplicates_1(self):
        self.assertEqual("aa", Solution().removeDuplicates("deeedbbcccbdaa", 3))

    def test_removeDuplicates_2(self):
        self.assertEqual("ps", Solution().removeDuplicates("pbbcggttciiippooaais", 2))
