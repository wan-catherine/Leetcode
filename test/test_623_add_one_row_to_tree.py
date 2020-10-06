from unittest import TestCase
from problems.N623_Add_One_Row_To_Tree import Solution
from problems.Utility_Tree import list_to_tree_node, treenode_to_list, null

class TestSolution(TestCase):
    def test_addOneRow(self):
        root = list_to_tree_node([4,2,6,3,1,5])
        self.assertListEqual([4,1,1,2,null,null,6,3,1,5], treenode_to_list(Solution().addOneRow(root, 1, 2)))
