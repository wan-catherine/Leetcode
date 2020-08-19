from unittest import TestCase
from problems.N556_Next_Greater_Element_III import Solution

class TestSolution(TestCase):
    def test_nextGreaterElement(self):
        self.assertEqual(21, Solution().nextGreaterElement(12))

    def test_nextGreaterElement_1(self):
        self.assertEqual(-1, Solution().nextGreaterElement(21))

    def test_nextGreaterElement_2(self):
        self.assertEqual(230412, Solution().nextGreaterElement(230241))

    def test_nextGreaterElement_3(self):
        self.assertEqual(13222344, Solution().nextGreaterElement(12443322))

    def test_nextGreaterElement_4(self):
        self.assertEqual(-1, Solution().nextGreaterElement(1999999999))
