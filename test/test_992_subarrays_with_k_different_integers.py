from unittest import TestCase
from problems.N992_Subarrays_With_K_Different_Integers import Solution

class TestSolution(TestCase):
    def test_subarraysWithKDistinct(self):
        self.assertEqual(7, Solution().subarraysWithKDistinct(A = [1,2,1,2,3], K = 2))

    def test_subarraysWithKDistinct_1(self):
        self.assertEqual(3, Solution().subarraysWithKDistinct(A = [1,2,1,3,4], K = 3))
