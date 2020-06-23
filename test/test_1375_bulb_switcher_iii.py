from unittest import TestCase
from problems.N1375_Bulb_Switcher_III import Solution

class TestSolution(TestCase):
    def test_numTimesAllBlue(self):
        self.assertEqual(3, Solution().numTimesAllBlue([2,1,3,5,4]))

    def test_numTimesAllBlue_1(self):
        self.assertEqual(2, Solution().numTimesAllBlue([3,2,4,1,5]))

    def test_numTimesAllBlue_2(self):
        self.assertEqual(1, Solution().numTimesAllBlue([4,1,2,3]))

    def test_numTimesAllBlue_3(self):
        self.assertEqual(3, Solution().numTimesAllBlue([2,1,4,3,6,5]))

    def test_numTimesAllBlue_4(self):
        self.assertEqual(6, Solution().numTimesAllBlue([1,2,3,4,5,6]))
