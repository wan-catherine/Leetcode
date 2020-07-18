from unittest import TestCase
from problems.N1386_Cinema_Seat_Allocation import Solution

class TestSolution(TestCase):
    def test_maxNumberOfFamilies(self):
        n = 3
        reservedSeats = [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]
        self.assertEqual(4, Solution().maxNumberOfFamilies(n, reservedSeats))

    def test_maxNumberOfFamilies_1(self):
        n = 4
        reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
        self.assertEqual(4, Solution().maxNumberOfFamilies(n, reservedSeats))

    def test_maxNumberOfFamilies_2(self):
        n = 2
        reservedSeats = [[2,1],[1,8],[2,6]]
        self.assertEqual(2, Solution().maxNumberOfFamilies(n, reservedSeats))
