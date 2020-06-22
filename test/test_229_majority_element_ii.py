from unittest import TestCase
from problems.N229_Majority_Element_II import Solution

class TestSolution(TestCase):
    def test_majorityElement(self):
        self.assertListEqual([3], Solution().majorityElement([3,2,3]))

    def test_majorityElement_1(self):
        self.assertListEqual([1,2], Solution().majorityElement([1,1,1,3,3,2,2,2]))

    def test_majorityElement_2(self):
        self.assertListEqual([1,2], Solution().majorityElement([1,2]))

    def test_majorityElement_3(self):
        self.assertListEqual([1], Solution().majorityElement([1,1,1,2,3,4,5,6]))
