from unittest import TestCase
from problems.N988_Smallest_String_Starting_From_Leaf import Solution
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_smallestFromLeaf(self):
        self.assertEqual("dba", Solution().smallestFromLeaf(list_to_tree_node([0,1,2,3,4,3,4])))

    def test_smallestFromLeaf_1(self):
        self.assertEqual("adz", Solution().smallestFromLeaf(list_to_tree_node([25,1,3,1,3,0,2])))

    def test_smallestFromLeaf_2(self):
        self.assertEqual("abc", Solution().smallestFromLeaf(list_to_tree_node([2,2,1,null,1,0,null,0])))

    def test_smallestFromLeaf_3(self):
        self.assertEqual("ba", Solution().smallestFromLeaf(list_to_tree_node([0,null,1])))
