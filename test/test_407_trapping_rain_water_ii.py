from unittest import TestCase
from problems.N407_Trapping_Rain_Water_II import Solution

class TestSolution(TestCase):
    def test_trapRainWater(self):
        self.assertEqual(4, Solution().trapRainWater([
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]))

    def test_trapRainWater_1(self):
        self.assertEqual(14, Solution().trapRainWater([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]))
