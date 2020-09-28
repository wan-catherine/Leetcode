from unittest import TestCase
from problems.N331_Verify_Preorder_Serialization_Of_A_Binary_Tree import Solution

class TestSolution(TestCase):
    def test_isValidSerialization(self):
        self.assertTrue(Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))

    def test_isValidSerialization_1(self):
        self.assertFalse(Solution().isValidSerialization("1,#"))

    def test_isValidSerialization_2(self):
        self.assertFalse(Solution().isValidSerialization("9,#,#,1"))

    def test_isValidSerialization_3(self):
        self.assertTrue(Solution().isValidSerialization("#"))

    def test_isValidSerialization_4(self):
        self.assertFalse(Solution().isValidSerialization("1,#,#,#,#"))

    def test_isValidSerialization_5(self):
        self.assertTrue(Solution().isValidSerialization("9,#,92,#,#"))

    def test_isValidSerialization_6(self):
        self.assertFalse(Solution().isValidSerialization("9,3,4,#,#,1,#,#,#,2,#,6,#,#"))

