from unittest import TestCase
from problems.N540_Single_Element_In_A_Sorted_Array import Solution

class TestSolution(TestCase):
    def test_singleNonDuplicate(self):
        self.assertEqual(2, Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8]))

    def test_singleNonDuplicate_1(self):
        self.assertEqual(10, Solution().singleNonDuplicate([3,3,7,7,10,11,11]))
