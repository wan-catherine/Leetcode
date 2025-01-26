from unittest import TestCase
from problems.N2127_Maximum_Employees_To_Be_Invited_To_A_Meeting import Solution

class TestSolution(TestCase):
    def test_maximum_invitations(self):
        self.assertEquals(3, Solution().maximumInvitations(favorite = [2,2,1,2]))

    def test_maximum_invitations_1(self):
        self.assertEquals(3, Solution().maximumInvitations([1,2,0]))

    def test_maximum_invitations_2(self):
        self.assertEquals(4, Solution().maximumInvitations([3,0,1,4,1]))
