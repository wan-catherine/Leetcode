from unittest import TestCase
from problems.N1367_Linked_List_In_Binary_Tree import Solution
from problems.Utility import create_linklist_from_list
from problems.Utility_Tree import null, list_to_tree_node

class TestSolution(TestCase):
    def test_isSubPath(self):
        head = create_linklist_from_list([2,8,3])
        root = list_to_tree_node([1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3])
        self.assertTrue(Solution().isSubPath(head, root))

    def test_isSubPath_1(self):
        head = create_linklist_from_list([1,4,2,6])
        root = list_to_tree_node([1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3])
        self.assertTrue(Solution().isSubPath(head, root))

    def test_isSubPath_2(self):
        head = create_linklist_from_list([1,4,2,6,8])
        root = list_to_tree_node([1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3])
        self.assertFalse(Solution().isSubPath(head, root))
