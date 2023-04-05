from unittest import TestCase
from problems.MajorityElement import Solution

class TestSolution(TestCase):
    def test_majorityElement(self):
        solution = Solution()
        res = solution.majorityElement([3,2,3])
        self.assertEqual(3, res)

    def test_majorityElement_one(self):
        solution = Solution()
        res = solution.majorityElement([2,2,1,1,1,2,2])
        self.assertEqual(2, res)
