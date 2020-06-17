from unittest import TestCase
from problems.N1109_Corporate_Flight_Bookings import Solution

class TestSolution(TestCase):
    def test_corpFlightBookings(self):
        bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
        n = 5
        self.assertListEqual([10,55,45,25,25], Solution().corpFlightBookings(bookings, n))
