from unittest import TestCase
from problems.N1110_Delete_Nodes_And_Return_Forest import Solution
from problems.Utility_Tree import list_to_tree_node, null, treenode_to_list

class TestSolution(TestCase):
    def test_delNodes(self):
        root = list_to_tree_node([1,2,3,4,5,6,7])
        res = Solution().delNodes(root, [3,5])
        output = []
        for r in res:
            output.append(treenode_to_list(r))
        self.assertListEqual([[1,2,null,4],[6],[7]], output)
