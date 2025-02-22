from unittest import TestCase
from problems.Utility_Tree import treenode_to_list, null
from problems.N1028_Recover_A_Tree_From_Preorder_Traversal import Solution

class TestSolution(TestCase):
    def test_recoverFromPreorder(self):
        self.assertListEqual([1,2,5,3,4,6,7], treenode_to_list(Solution().recoverFromPreorder("1-2--3--4-5--6--7")))

    def test_recoverFromPreorder_1(self):
        self.assertListEqual([1,2,5,3,null,6,null,4,null,7], treenode_to_list(Solution().recoverFromPreorder("1-2--3---4-5--6---7")))

    def test_recoverFromPreorder_2(self):
        self.assertListEqual([1,401,null,349,88,90], treenode_to_list(Solution().recoverFromPreorder("1-401--349---90--88")))
