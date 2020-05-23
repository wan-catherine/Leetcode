from unittest import TestCase
from problems.N18_4Sum import Solution

class TestSolution(TestCase):
    def test_fourSum(self):
        output = [
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
        res = Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
        for li in res:
            self.assertIn(li, output)
        self.assertEqual(len(output), len(res))

    def test_fourSum_1(self):
        output = [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        res = Solution().fourSum([-3,-2,-1,0,0,1,2,3], 0)
        for li in res:
            self.assertIn(li, output)
        self.assertEqual(len(output), len(res))

    def test_fourSum_2(self):
        output = [[-5,-4,-1,1],[-5,-4,0,0],[-5,-2,-2,0],[-4,-2,-2,-1]]
        res = Solution().fourSum([-1,0,-5,-2,-2,-4,0,1,-2], -9)
        for li in res:
            self.assertIn(li, output)
        self.assertEqual(len(output), len(res))