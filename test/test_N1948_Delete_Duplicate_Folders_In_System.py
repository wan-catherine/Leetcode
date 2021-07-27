from unittest import TestCase
from problems.N1948_Delete_Duplicate_Folders_In_System import Solution

class TestSolution(TestCase):
    def test_delete_duplicate_folder(self):
        self.assertListEqual([["d"],["d","a"]], Solution().deleteDuplicateFolder([["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]))

    def test_delete_duplicate_folder_1(self):
        self.assertListEqual([["c"],["c","b"],["a"],["a","b"]], Solution().deleteDuplicateFolder([["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]))

    def test_delete_duplicate_folder_2(self):
        self.assertListEqual([["c"],["c","d"],["a"],["a","b"]], Solution().deleteDuplicateFolder([["a","b"],["c","d"],["c"],["a"]]))

    def test_delete_duplicate_folder_3(self):
        self.assertListEqual([], Solution().deleteDuplicateFolder([["a"],["a","x"],["a","x","y"],["a","z"],["b"],["b","x"],["b","x","y"],["b","z"]]))

    def test_delete_duplicate_folder_4(self):
        self.assertListEqual([["b"],["b","w"],["b","z"],["a"],["a","z"]], Solution().deleteDuplicateFolder([["a"],["a","x"],["a","x","y"],["a","z"],["b"],["b","x"],["b","x","y"],["b","z"],["b","w"]]))

    def test_delete_duplicate_folder_5(self):
        self.assertListEqual([["b"],["f"],["l"],["c"],["h"],["f","r"],["f","o"],["l","q"],["h","t"],["f","r","g"],["f","o","l"],["f","r","g","c"],["f","r","g","c","r"]], Solution().deleteDuplicateFolder([["b"],["f"],["f","r"],["f","r","g"],["f","r","g","c"],["f","r","g","c","r"],["f","o"],["f","o","x"],["f","o","x","t"],["f","o","x","d"],["f","o","l"],["l"],["l","q"],["c"],["h"],["h","t"],["h","o"],["h","o","d"],["h","o","t"]]))
