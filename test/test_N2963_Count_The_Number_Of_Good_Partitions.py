from unittest import TestCase
from problems.N2963_Count_The_Number_Of_Good_Partitions import Solution

class TestSolution(TestCase):
    def test_number_of_good_partitions(self):
        self.assertEquals(8, Solution().numberOfGoodPartitions([1,2,3,4]))

    def test_number_of_good_partitions_1(self):
        self.assertEquals(1, Solution().numberOfGoodPartitions([1,1,1,1]))

    def test_number_of_good_partitions_2(self):
        self.assertEquals(2, Solution().numberOfGoodPartitions([1,2,1,3]))

    def test_number_of_good_partitions_3(self):
        self.assertEquals(8, Solution().numberOfGoodPartitions([1,1,5,9,2]))
