from unittest import TestCase
from problems.N982_Triples_With_Bitwise_And_Equal_To_Zero import Solution

class TestSolution(TestCase):
    def test_count_triplets(self):
        self.assertEqual(12, Solution().countTriplets([2,1,3]))