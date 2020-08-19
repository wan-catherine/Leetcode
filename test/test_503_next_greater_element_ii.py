from unittest import TestCase
from problems.N503_Next_Greater_Element_II import Solution

class TestSolution(TestCase):
    def test_nextGreaterElements(self):
        self.assertListEqual([2,-1,2], Solution().nextGreaterElements([1,2,1]))

    def test_nextGreaterElements_1(self):
        self.assertListEqual([-1,5,5,5,5], Solution().nextGreaterElements([5,4,3,2,1]))
