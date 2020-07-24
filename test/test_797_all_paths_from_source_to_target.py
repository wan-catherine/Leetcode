from unittest import TestCase
from problems.N797_All_Paths_From_Source_To_Target import Solution

class TestSolution(TestCase):
    def test_allPathsSourceTarget(self):
        self.assertListEqual([[0,1,3],[0,2,3]], Solution().allPathsSourceTarget([[1,2], [3], [3], []]))
