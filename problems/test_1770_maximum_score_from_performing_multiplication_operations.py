from unittest import TestCase
from problems.N1770_Maximum_Score_From_Performing_Multiplication_Operations import Solution

class TestSolution(TestCase):
    def test_maximumScore(self):
        self.assertEqual(14, Solution().maximumScore(nums = [1,2,3], multipliers = [3,2,1]))

    def test_maximumScore_1(self):
        self.assertEqual(102, Solution().maximumScore(nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]))

    def test_maximumScore_2(self):
        self.assertEqual(6861161, Solution().maximumScore([555,526,732,182,43,-537,-434,-233,-947,968,-250,-10,470,-867,-809,-987,120,607,-700,25,-349,-657,349,-75,-936,-473,615,691,-261,-517,-867,527,782,939,-465,12,988,-78,-990,504,-358,491,805,756,-218,513,-928,579,678,10],
                                                      [783,911,820,37,466,-251,286,-74,-899,586,792,-643,-969,-267,121,-656,381,871,762,-355,721,753,-521]))
