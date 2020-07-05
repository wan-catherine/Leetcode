from unittest import TestCase
from problems.N825_Friends_Of_Appropriate_Ages import Solution

class TestSolution(TestCase):
    def test_numFriendRequests(self):
        self.assertEqual(2, Solution().numFriendRequests([16,16]))

    def test_numFriendRequests_1(self):
        self.assertEqual(3, Solution().numFriendRequests([20,30,100,110,120]))

    def test_numFriendRequests_2(self):
        self.assertEqual(2, Solution().numFriendRequests([16,17,18]))
