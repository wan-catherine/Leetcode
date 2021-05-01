from unittest import TestCase
from problems.N1847_Closest_Room import Solution

class TestSolution(TestCase):
    def test_closest_room(self):
        self.assertListEqual([3,-1,3], Solution().closestRoom(rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]))

    def test_closest_room_1(self):
        self.assertListEqual([2,1,3], Solution().closestRoom(rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]))
