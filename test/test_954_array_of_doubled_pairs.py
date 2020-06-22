from unittest import TestCase
from problems.N954_Array_Of_Doubled_Pairs import Solution

class TestSolution(TestCase):
    def test_canReorderDoubled(self):
        self.assertFalse(Solution().canReorderDoubled([3,1,3,6]))

    def test_canReorderDoubled_1(self):
        self.assertFalse(Solution().canReorderDoubled([2,1,2,6]))

    def test_canReorderDoubled_2(self):
        self.assertFalse(Solution().canReorderDoubled([1,2,4,16,8,4]))

    def test_canReorderDoubled_3(self):
        self.assertTrue(Solution().canReorderDoubled([4,-2,2,-4]))

    def test_canReorderDoubled_4(self):
        self.assertTrue(Solution().canReorderDoubled([1,2,1,-8,8,-4,4,-4,2,-2]))

    def test_canReorderDoubled_5(self):
        self.assertTrue(Solution().canReorderDoubled([0,0]))

