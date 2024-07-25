from unittest import TestCase
from problems.N3181_Maximum_Total_Reward_Using_Operations_II import Solution

class TestSolution(TestCase):
    def test_max_total_reward(self):
        self.assertEquals(4, Solution().maxTotalReward([1,1,3,3]))

    def test_max_total_reward_1(self):
        self.assertEquals(11, Solution().maxTotalReward([1,6,4,3,2]))
