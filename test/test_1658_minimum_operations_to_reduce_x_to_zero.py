from unittest import TestCase
from problems.N1658_Minimum_Operation_To_Reduce_X_To_Zero import Solution

class TestSolution(TestCase):
    def test_minOperations(self):
        self.assertEqual(2, Solution().minOperations(nums = [1,1,4,2,3], x = 5))

    def test_minOperations_1(self):
        self.assertEqual(-1, Solution().minOperations(nums = [5,6,7,8,9], x = 4))

    def test_minOperations_2(self):
        self.assertEqual(5, Solution().minOperations(nums = [3,2,20,1,1,3], x = 10))

    def test_minOperations_3(self):
        self.assertEqual(16, Solution().minOperations([8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], 134365))
