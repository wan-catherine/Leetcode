from unittest import TestCase
from problems.PathSumII import TreeNode, Solution
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_pathSum(self):
        head = list_to_tree_node([5,4,8,11,null,13,4,7,2,null,null,5,1])
        expected =[
   [5,4,11,2],
   [5,8,4,5]
]
        self.assertListEqual(expected, Solution().pathSum(head, 22))

