from unittest import TestCase
from problems.N2968_Apply_Operations_To_Maximize_Frequency_Score import Solution

class TestSolution(TestCase):
    def test_max_frequency_score(self):
        self.assertEquals(3, Solution().maxFrequencyScore(nums = [1,2,6,4], k = 3))

    def test_max_frequency_score_1(self):
        self.assertEquals(3, Solution().maxFrequencyScore(nums = [1,4,4,2,4], k = 0))
