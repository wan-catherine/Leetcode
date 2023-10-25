from unittest import TestCase
from problems.N2910_Minimum_Number_Of_Groups_To_Create_A_Valid_Assignment import Solution

class TestSolution(TestCase):
    def test_min_groups_for_valid_assignment(self):
        self.assertEquals(2, Solution().minGroupsForValidAssignment([3,2,3,2,3]))

    def test_min_groups_for_valid_assignment_1(self):
        self.assertEquals(4, Solution().minGroupsForValidAssignment([10,10,10,3,1,1]))
