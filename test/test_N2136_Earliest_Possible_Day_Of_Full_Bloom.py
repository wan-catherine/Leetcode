from unittest import TestCase
from problems.N2136_Earliest_Possible_Day_Of_Full_Bloom import Solution

class TestSolution(TestCase):
    def test_earliest_full_bloom(self):
        self.assertEqual(9, Solution().earliestFullBloom(plantTime = [1,4,3], growTime = [2,3,1]))

    def test_earliest_full_bloom_1(self):
        self.assertEqual(9, Solution().earliestFullBloom(plantTime = [1,2,3,2], growTime = [2,1,2,1]))

    def test_earliest_full_bloom_2(self):
        self.assertEqual(9, Solution().earliestFullBloom(plantTime = [1], growTime = [1]))
