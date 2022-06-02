from unittest import TestCase
from problems.N253_Meeting_Rooms_II import Solution

class TestSolution(TestCase):
    def test_min_meeting_rooms(self):
        self.assertEqual(2, Solution().minMeetingRooms([[0,30],[5,10],[15,20]]))

    def test_min_meeting_rooms_1(self):
        self.assertEqual(1, Solution().minMeetingRooms([[7,10],[2,4]]))

    def test_min_meeting_rooms_2(self):
        self.assertEqual(2, Solution().minMeetingRooms([[9,10],[4,9],[4,17]]))
