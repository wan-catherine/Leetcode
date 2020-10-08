from unittest import TestCase
from problems.N951_Flip_Equivalent_Binary_Trees import Solution
from problems.Utility_Tree import list_to_tree_node,null

class TestSolution(TestCase):
    def test_flipEquiv(self):
        root1 = list_to_tree_node([1,2,3,4,5,6,null,null,null,7,8])
        root2 = list_to_tree_node([1,3,2,null,6,4,5,null,null,null,null,8,7])
        self.assertTrue(Solution().flipEquiv(root1, root2))

    def test_flipEquiv_1(self):
        root1 = list_to_tree_node([])
        root2 = list_to_tree_node([])
        self.assertTrue(Solution().flipEquiv(root1, root2))

    def test_flipEquiv_2(self):
        root1 = list_to_tree_node([])
        root2 = list_to_tree_node([1])
        self.assertFalse(Solution().flipEquiv(root1, root2))

    def test_flipEquiv_3(self):
        root1 = list_to_tree_node([0,null,1])
        root2 = list_to_tree_node([])
        self.assertFalse(Solution().flipEquiv(root1, root2))

    def test_flipEquiv_4(self):
        root1 = list_to_tree_node([0,null,1])
        root2 = list_to_tree_node([0,1])
        self.assertTrue(Solution().flipEquiv(root1, root2))
