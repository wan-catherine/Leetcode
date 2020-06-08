from unittest import TestCase
from problems.N448_Find_All_Numbers_Disappeared_In_An_Array import Solution

class TestSolution(TestCase):
    def test_findDisappearedNumbers(self):
        self.assertListEqual([5,6], Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))
