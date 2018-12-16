from unittest import TestCase
from problems.ContainsDuplicateIII import Solution

class TestSolution(TestCase):
    def test_containsNearbyAlmostDuplicate(self):
        solution = Solution()
        res = solution.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0)
        self.assertEqual(True, res)

    def test_containsNearbyAlmostDuplicate_three(self):
        solution = Solution()
        res = solution.containsNearbyAlmostDuplicate([2,1], 1, 1)
        self.assertEqual(True, res)

    def test_containsNearbyAlmostDuplicate_one(self):
        solution = Solution()
        res = solution.containsNearbyAlmostDuplicate([1,0,1,1], 1, 2)
        self.assertEqual(True, res)

    def test_containsNearbyAlmostDuplicate_two(self):
        solution = Solution()
        res = solution.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3)
        self.assertEqual(False, res)