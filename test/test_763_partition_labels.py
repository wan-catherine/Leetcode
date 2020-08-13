from unittest import TestCase
from problems.N763_Partition_Labels import Solution

class TestSolution(TestCase):
    def test_partitionLabels(self):
        self.assertListEqual([9,7,8], Solution().partitionLabels("ababcbacadefegdehijhklij"))

    def test_partitionLabels_1(self):
        self.assertListEqual([9,1], Solution().partitionLabels("eaaaabaaec"))
