from unittest import TestCase
from problems.N1203_Sort_Items_By_Groups_Respecting_Dependencies import Solution

class TestSolution(TestCase):
    def test_sortItems(self):
        self.assertListEqual([0, 5, 2, 6, 3, 4, 7, 1], Solution().sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]))

    def test_sortItems_1(self):
        self.assertListEqual([], Solution().sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]))

    def test_sortItems_2(self):
        self.assertListEqual([2, 3, 4, 1, 0], Solution().sortItems(n = 5, m = 5, group = [2,0,-1,3,0], beforeItems = [[2,1,3],[2,4],[],[],[]]))

    def test_sortItems_3(self):
        self.assertListEqual([2, 3, 0, 1, 4], Solution().sortItems(5, 3, [0,0,2,1,0], [[3],[],[],[],[1,3,2]]))
