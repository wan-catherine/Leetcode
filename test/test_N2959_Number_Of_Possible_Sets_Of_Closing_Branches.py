from unittest import TestCase
from problems.N2959_Number_Of_Possible_Sets_Of_Closing_Branches import Solution

class TestSolution(TestCase):
    def test_number_of_sets(self):
        self.assertEquals(5, Solution().numberOfSets(n = 3, maxDistance = 5, roads = [[0,1,2],[1,2,10],[0,2,10]]))

    def test_number_of_sets_1(self):
        self.assertEquals(7, Solution().numberOfSets(n = 3, maxDistance = 5, roads = [[0,1,20],[0,1,10],[1,2,2],[0,2,2]]))

    def test_number_of_sets_2(self):
        self.assertEquals(2, Solution().numberOfSets(n = 1, maxDistance = 10, roads = []))

    def test_number_of_sets_3(self):
        self.assertEquals(6, Solution().numberOfSets(n = 3, maxDistance = 5, roads = [[2,0,4],[1,0,3],[1,0,2]]))
