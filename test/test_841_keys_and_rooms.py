from unittest import TestCase
from problems.N841_Keys_And_Rooms import Solution

class TestSolution(TestCase):
    def test_canVisitAllRooms(self):
        self.assertTrue(Solution().canVisitAllRooms([[1],[2],[3],[]]))

    def test_canVisitAllRooms_1(self):
        self.assertFalse(Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))

