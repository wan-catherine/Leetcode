from unittest import TestCase
from problems.N1815_Maximum_Number_Of_Groups_Getting_Fresh_Donuts import Solution

class TestSolution(TestCase):
    def test_max_happy_groups(self):
        self.assertEqual(4, Solution().maxHappyGroups(batchSize = 3, groups = [1,2,3,4,5,6]))

    def test_max_happy_groups_1(self):
        self.assertEqual(4, Solution().maxHappyGroups(batchSize = 4, groups = [1,3,2,5,2,2,1,6]))
