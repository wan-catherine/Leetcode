from unittest import TestCase
from problems.N1233_Remove_Sub_Folders_From_The_Filesystem import Solution

class TestSolution(TestCase):
    def test_removeSubfolders(self):
        folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
        self.assertListEqual(["/a","/c/d","/c/f"], Solution().removeSubfolders(folder))

    def test_removeSubfolders_1(self):
        folder = ["/a","/a/b/c","/a/b/d"]
        self.assertListEqual(["/a"], Solution().removeSubfolders(folder))

    def test_removeSubfolders_2(self):
        folder = ["/a/b/c","/a/b/ca","/a/b/d"]
        self.assertListEqual(["/a/b/c","/a/b/ca","/a/b/d"], Solution().removeSubfolders(folder))