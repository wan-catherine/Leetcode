from unittest import TestCase
from problems.N1296_Divide_Array_In_Sets_Of_K_Consecutive_Numbers import Solution

class TestSolution(TestCase):
    def test_isPossibleDivide(self):
        self.assertTrue(Solution().isPossibleDivide(nums = [1,2,3,3,4,4,5,6], k = 4))

    def test_isPossibleDivide_1(self):
        self.assertTrue(Solution().isPossibleDivide(nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3))

    def test_isPossibleDivide_2(self):
        self.assertTrue(Solution().isPossibleDivide(nums = [3,3,2,2,1,1], k = 3))

    def test_isPossibleDivide_3(self):
        self.assertFalse(Solution().isPossibleDivide(nums = [1,2,3,4], k = 3))

    def test_isPossibleDivide_4(self):
        self.assertFalse(Solution().isPossibleDivide(nums = [2,4,6], k = 3))

    def test_isPossibleDivide_5(self):
        self.assertFalse(Solution().isPossibleDivide([1,1,2,2,3,3],2))

    def test_isPossibleDivide_6(self):
        nums = [9,13,15,23,22,25,4,4,29,15,8,23,12,19,24,17,18,11,22,24,17,17,10,23,21,18,14,18,7,6,3,6,19,11,16,11,12,13,8,26,17,20,13,19,22,21,27,9,20,15,20,27,8,13,25,23,22,15,9,14,20,10,6,5,14,12,7,16,21,18,21,24,23,10,21,16,18,16,18,5,20,19,20,10,14,26,2,9,19,12,28,17,5,7,25,22,16,17,21,11]
        k = 10
        self.assertFalse(Solution().isPossibleDivide(nums, k))

    def test_isPossibleDivide_7(self):
        nums =[19,17,18,15,23,23,20,16,21,18,20,5,22,27,19,20,19,11,8,14,10,21,20,14,19,7,15,25,20,22,16,17,28,13,6,11,14,17,20,21,13,8,10,6,10,20,26,24,13,9,15,18,17,7,16,13,3,16,16,18,9,24,19,24,23,4,18,17,15,23,1,12,2,15,14,14,25,22,19,9,24,12,13,29,22,25,12,21,18,26,12,27,21,15,22,11,17,26,11,8]
        k = 10
        self.assertTrue(Solution().isPossibleDivide(nums, k))
