from unittest import TestCase
from problems.N1409_Queries_On_A_Permutation_With_Key import Solution

class TestSolution(TestCase):
    def test_processQueries(self):
        self.assertListEqual([2,1,2,1], Solution().processQueries([3,1,2,1], 5))

    def test_processQueries_1(self):
        self.assertListEqual([3,1,2,0], Solution().processQueries([4,1,2,2], 4))

    def test_processQueries_2(self):
        self.assertListEqual([6,5,0,7,5], Solution().processQueries([7,5,5,8,3], 8))

