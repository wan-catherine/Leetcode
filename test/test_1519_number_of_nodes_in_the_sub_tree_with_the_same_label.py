from unittest import TestCase
from problems.N1519_Number_Of_Nodes_In_The_Sub_Tree_With_The_Same_Label import Solution

class TestSolution(TestCase):
    def test_countSubTrees(self):
        self.assertListEqual([2,1,1,1,1,1,1], Solution().countSubTrees(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"))

    def test_countSubTrees_1(self):
        self.assertListEqual([4,2,1,1], Solution().countSubTrees(n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"))

    def test_countSubTrees_2(self):
        self.assertListEqual([3,2,1,1,1], Solution().countSubTrees(n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"))

    def test_countSubTrees_3(self):
        self.assertListEqual([1,2,1,1,2,1], Solution().countSubTrees(n = 6, edges = [[0,1],[0,2],[1,3],[3,4],[4,5]], labels = "cbabaa"))

    def test_countSubTrees_4(self):
        self.assertListEqual([6,5,4,1,3,2,1], Solution().countSubTrees(n = 7, edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], labels = "aaabaaa"))

    def test_countSubTrees_5(self):
        self.assertListEqual([1,1,2,1], Solution().countSubTrees(4, [[0,2],[0,3],[1,2]], "aeed"))
