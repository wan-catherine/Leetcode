from unittest import TestCase
from problems.N2478_Number_Of_Beautiful_Partitions import Solution

class TestSolution(TestCase):
    def test_beautiful_partitions(self):
        self.assertEqual(3, Solution().beautifulPartitions(s = "23542185131", k = 3, minLength = 2))

    def test_beautiful_partitions_1(self):
        self.assertEqual(1, Solution().beautifulPartitions(s = "23542185131", k = 3, minLength = 3))

    def test_beautiful_partitions_2(self):
        self.assertEqual(1, Solution().beautifulPartitions(s = "3312958", k = 3, minLength = 1))
