from unittest import TestCase
from problems.N287_Find_The_Duplicate_Number import Solution

class TestSolution(TestCase):
    def test_findDuplicate(self):
        self.assertEqual(2, Solution().findDuplicate([1,3,4,2,2]))

    def test_findDuplicate_1(self):
        self.assertEqual(3, Solution().findDuplicate([3,1,3,4,2]))
