from unittest import TestCase
from problems.N698_Partition_To_K_Equal_Sum_Subsets import Solution

class TestSolution(TestCase):
    def test_canPartitionKSubsets(self):
        self.assertTrue(Solution().canPartitionKSubsets(nums = [4, 3, 2, 3, 5, 2, 1], k = 4))

    def test_canPartitionKSubsets_1(self):
        self.assertFalse(Solution().canPartitionKSubsets([2,2,2,2,3,4,5], 4))

    def test_canPartitionKSubsets_2(self):
        self.assertTrue(Solution().canPartitionKSubsets([815,625,3889,4471,60,494,944,1118,4623,497,771,679,1240,202,601,883], 3))

    def test_canPartitionKSubsets_3(self):
        self.assertFalse(Solution().canPartitionKSubsets([85,35,40,64,86,45,63,16,5364,110,5653,97,95], 7))

    def test_canPartitionKSubsets_4(self):
        self.assertTrue(Solution().canPartitionKSubsets([10,10,10,7,7,7,7,7,7,6,6,6], 3))
