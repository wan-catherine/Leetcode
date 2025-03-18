from unittest import TestCase
from problems.N3134_Find_The_Median_Of_The_Uniqueness_Array import Solution

class TestSolution(TestCase):
    def test_median_of_uniqueness_array(self):
        self.assertEquals(1, Solution().medianOfUniquenessArray([1,2,3]))

    def test_median_of_uniqueness_array_1(self):
        self.assertEquals(2, Solution().medianOfUniquenessArray([3,4,3,4,5]))

    def test_median_of_uniqueness_array_2(self):
        self.assertEquals(2, Solution().medianOfUniquenessArray([4,3,5,4]))

    def test_median_of_uniqueness_array_3(self):
        self.assertEquals(1, Solution().medianOfUniquenessArray([8,8,8]))

    def test_median_of_uniqueness_array_4(self):
        self.assertEquals(2, Solution().medianOfUniquenessArray([4,21,43,21,43,4,43,21]))
