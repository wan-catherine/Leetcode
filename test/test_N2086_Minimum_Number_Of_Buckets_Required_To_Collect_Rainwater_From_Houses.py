from unittest import TestCase
from problems.N2086_Minimum_Number_Of_Buckets_Required_To_Collect_Rainwater_From_Houses import Solution

class TestSolution(TestCase):
    def test_minimum_buckets(self):
        self.assertEqual(1, Solution().minimumBuckets(".H.H."))
