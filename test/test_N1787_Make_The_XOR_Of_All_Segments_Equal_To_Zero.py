from unittest import TestCase
from problems.N1787_Make_The_XOR_Of_All_Segments_Equal_To_Zero import Solution

class TestSolution(TestCase):
    def test_min_changes(self):
        self.assertEqual(3, Solution().minChanges(nums = [1,2,0,3,0], k = 1))

    def test_min_changes_1(self):
        self.assertEqual(3, Solution().minChanges(nums = [3,4,5,2,1,7,3,4,7], k = 3))

    def test_min_changes_2(self):
        self.assertEqual(3, Solution().minChanges([1,2,4,1,2,5,1,2,6], k = 3))

    def test_min_changes_3(self):
        self.assertEqual(11, Solution().minChanges([26,19,19,28,13,14,6,25,28,19,0,15,25,11], 3))

    def test_min_changes_4(self):
        self.assertEqual(20, Solution().minChanges([6,31,21,6,14,15,19,13,9,19,27,10,16,10,3,7,27,21,28,8,0,14,17,11,0,12,6,0], 8))
