from unittest import TestCase
from problems.N1617_Count_Subtrees_With_Max_Distance_Between_Cities import Solution

class TestSolution(TestCase):
    def test_countSubgraphsForEachDiameter(self):
        self.assertListEqual([3,4,0], Solution().countSubgraphsForEachDiameter(n = 4, edges = [[1,2],[2,3],[2,4]]))

    def test_countSubgraphsForEachDiameter_1(self):
        self.assertListEqual([1], Solution().countSubgraphsForEachDiameter(n = 2, edges = [[1,2]]))

    def test_countSubgraphsForEachDiameter_2(self):
        self.assertListEqual([2,1], Solution().countSubgraphsForEachDiameter(n = 3, edges = [[1,2],[2,3]]))

    def test_countSubgraphsForEachDiameter_3(self):
        self.assertListEqual([3,2,1], Solution().countSubgraphsForEachDiameter(4, [[1,3],[1,4],[2,3]]))

