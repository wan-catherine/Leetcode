from unittest import TestCase
from problems.N442_Find_All_Duplicates_In_An_Array import Solution

class TestSolution(TestCase):
    def test_findDuplicates(self):
        self.assertListEqual([2,3], Solution().findDuplicates([4,3,2,7,8,2,3,1]))
