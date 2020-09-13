from unittest import TestCase
from problems.N1585_Check_If_String_Is_Transformable_With_Substring_Sort_Operations import Solution

class TestSolution(TestCase):
    def test_isTransformable(self):
        self.assertTrue(Solution().isTransformable(s = "84532", t = "34852"))

    def test_isTransformable_1(self):
        self.assertTrue(Solution().isTransformable(s = "34521", t = "23415"))

    def test_isTransformable_2(self):
        self.assertFalse(Solution().isTransformable(s = "12345", t = "12435"))

    def test_isTransformable_3(self):
        self.assertFalse(Solution().isTransformable(s = "1", t = "2"))