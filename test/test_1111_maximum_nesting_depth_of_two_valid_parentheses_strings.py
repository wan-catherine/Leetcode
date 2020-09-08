from unittest import TestCase
from problems.N1111_Maximum_Nesting_Depth_Of_Two_Valid_Parentheses_Strings import Solution

class TestSolution(TestCase):
    def test_maxDepthAfterSplit(self):
        self.assertListEqual([0,1,1,1,1,0], Solution().maxDepthAfterSplit("(()())"))

    def test_maxDepthAfterSplit_1(self):
        self.assertListEqual([0,0,0,1,1,0,1,1], Solution().maxDepthAfterSplit("()(())()"))
