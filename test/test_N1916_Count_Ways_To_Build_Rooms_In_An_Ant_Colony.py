from unittest import TestCase
from problems.N1916_Count_Ways_To_Build_Rooms_In_An_Ant_Colony import Solution

class TestSolution(TestCase):
    def test_ways_to_build_rooms(self):
        self.assertEqual(1, Solution().waysToBuildRooms([-1,0,1]))

    def test_ways_to_build_rooms_1(self):
        self.assertEqual(6, Solution().waysToBuildRooms([-1,0,0,1,2]))

    def test_ways_to_build_rooms_2(self):
        self.assertEqual(3, Solution().waysToBuildRooms([-1,0,1,2,1]))
