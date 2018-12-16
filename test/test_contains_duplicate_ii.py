from unittest import TestCase
from problems.ContainsDuplicateII import Solution

class TestSolution(TestCase):
    def test_containsNearbyDuplicate(self):
        solution = Solution()
        res = solution.containsNearbyDuplicate([1,2,3,1], 3)
        self.assertEqual(True, res)

    def test_containsNearbyDuplicate_one(self):
        solution = Solution()
        res = solution.containsNearbyDuplicate([1,0,1,1], 1)
        self.assertEqual(True, res)

    def test_containsNearbyDuplicate_two(self):
        solution = Solution()
        res = solution.containsNearbyDuplicate([1,2,3,1,2,3], 2)
        self.assertEqual(False, res)