from unittest import TestCase
from problems.N1526_Minimum_Number_Of_Increments_On_Subarrays_To_Form_A_Target_Array import Solution

class TestSolution(TestCase):
    def test_minNumberOperations(self):
        target = [1, 2, 3, 2, 1]
        self.assertEqual(3, Solution().minNumberOperations(target))

    def test_minNumberOperations_1(self):
        target = [3,1,1,2]
        self.assertEqual(4, Solution().minNumberOperations(target))

    def test_minNumberOperations_2(self):
        target = [3,1,5,4,2]
        self.assertEqual(7, Solution().minNumberOperations(target))

    def test_minNumberOperations_3(self):
        target = [1,1,1,1]
        self.assertEqual(1, Solution().minNumberOperations(target))
