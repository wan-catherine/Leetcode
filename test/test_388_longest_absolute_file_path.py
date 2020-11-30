from unittest import TestCase
from problems.N388_Longest_Absolute_File_Path import Solution

class TestSolution(TestCase):
    def test_lengthLongestPath(self):
        self.assertEqual(20, Solution().lengthLongestPath(r"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))

    def test_lengthLongestPath_1(self):
        self.assertEqual(32, Solution().lengthLongestPath(r"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))

    def test_lengthLongestPath_2(self):
        self.assertEqual(0, Solution().lengthLongestPath("a"))

    def test_lengthLongestPath_3(self):
        self.assertEqual(12, Solution().lengthLongestPath(r"file1.txt\nfile2.txt\nlongfile.txt"))