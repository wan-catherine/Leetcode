from unittest import TestCase
from problems.N1457_Pseudo_Palindromic_Paths_In_A_Binary_Tree import Solution
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_pseudoPalindromicPaths(self):
        self.assertEqual(2, Solution().pseudoPalindromicPaths(list_to_tree_node([2,3,1,3,1,null,1])))

    def test_pseudoPalindromicPaths_1(self):
        self.assertEqual(1, Solution().pseudoPalindromicPaths(list_to_tree_node([2,1,1,1,3,null,null,null,null,null,1])))

    def test_pseudoPalindromicPaths_2(self):
        self.assertEqual(1, Solution().pseudoPalindromicPaths(list_to_tree_node([9])))

    def test_pseudoPalindromicPaths_3(self):
        self.assertEqual(2, Solution().pseudoPalindromicPaths(list_to_tree_node([8,8,null,7,7,null,null,2,4,null,8,null,7,null,1])))

    def test_pseudoPalindromicPaths_4(self):
        self.assertEqual(0, Solution().pseudoPalindromicPaths(list_to_tree_node([1,5,null,7,null,3,9,null,3,1,null,4,null,null,4])))
