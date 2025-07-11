from unittest import TestCase
from problems.N2402_Meeting_Rooms_III import Solution

class TestSolution(TestCase):
    def test_most_booked(self):
        self.assertEquals(0, Solution().mostBooked(n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]))

    def test_most_booked_1(self):
        self.assertEquals(1, Solution().mostBooked(n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]))

    def test_most_booked_2(self):
        self.assertEquals(0, Solution().mostBooked(n = 4, meetings = [[18,19],[3,12],[17,19],[2,13],[7,10]]))
