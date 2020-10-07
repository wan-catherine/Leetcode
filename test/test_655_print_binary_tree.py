from unittest import TestCase
from problems.N655_Print_Binary_Tree import Solution
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_printTree(self):
        self.assertListEqual([["", "1", ""],["2", "", ""]], Solution().printTree(list_to_tree_node([1,2])))

    def test_printTree_1(self):
        self.assertListEqual([["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]], Solution().printTree(list_to_tree_node([1,2,3,null,4])))

    def test_printTree_2(self):
        self.assertListEqual([["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""],
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""],
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""],
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]], Solution().printTree(list_to_tree_node([1,2,5,3,null,null,null,4])))

