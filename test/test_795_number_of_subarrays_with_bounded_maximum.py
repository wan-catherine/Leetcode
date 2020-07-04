from unittest import TestCase
from problems.N795_Numbers_Of_Subarrays_With_Bounded_Maximum import Solution

class TestSolution(TestCase):
    def test_numSubarrayBoundedMax(self):
        self.assertEqual(3, Solution().numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))

    def test_numSubarrayBoundedMax_1(self):
        self.assertEqual(22, Solution().numSubarrayBoundedMax([73,55,36,5,55,14,9,7,72,52], 32, 69))

    def test_numSubarrayBoundedMax_2(self):
        self.assertEqual(7, Solution().numSubarrayBoundedMax([2,9,2,5,6], 2, 8))

    def test_numSubarrayBoundedMax_3(self):
        self.assertEqual(19, Solution().numSubarrayBoundedMax([876,880,482,260,132,421,732,703,795,420,871,445,400,291,358,589,617,202,755,810,227,813,549,791,418,528,835,401,526,584,873,662,13,314,988,101,299,816,833,224,160,852,179,769,646,558,661,808,651,982,878,918,406,551,467,87,139,387,16,531,307,389,939,551,613,36,528,460,404,314,66,111,458,531,944,461,951,419,82,896,467,353,704,905,705,760,61,422,395,298,127,516,153,299,801,341,668,598,98,241]
,658,719))