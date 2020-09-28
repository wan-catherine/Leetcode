from unittest import TestCase
from problems.N1601_Maximum_Number_Of_Achievable_Transfer_Requests import Solution

class TestSolution(TestCase):
    def test_maximumRequests(self):
        self.assertEqual(5, Solution().maximumRequests(n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]))

    def test_maximumRequests_1(self):
        self.assertEqual(3, Solution().maximumRequests(n = 3, requests = [[0,0],[1,2],[2,1]]))

    def test_maximumRequests_2(self):
        self.assertEqual(4, Solution().maximumRequests(n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]))
