from unittest import TestCase
from problems.N2790_Maximum_Number_Of_Groups_With_Increasing_Length import Solution

class TestSolution(TestCase):
    def test_max_increasing_groups(self):
        self.assertEquals(3, Solution().maxIncreasingGroups([1,2,5]))

    def test_max_increasing_groups_1(self):
        self.assertEquals(2, Solution().maxIncreasingGroups([2,1,2]))

    def test_max_increasing_groups_2(self):
        self.assertEquals(1, Solution().maxIncreasingGroups([1,1]))

    def test_max_increasing_groups_3(self):
        self.assertEquals(3, Solution().maxIncreasingGroups([2,2,2]))
