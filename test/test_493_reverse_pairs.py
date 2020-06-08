from unittest import TestCase
from problems.N493_Reverse_Pairs import Solution

class TestSolution(TestCase):
    def test_reversePairs(self):
        self.assertEqual(2, Solution().reversePairs([1,3,2,3,1]))

    def test_reversePairs_1(self):
        self.assertEqual(3, Solution().reversePairs([2,4,3,5,1]))

    def test_reversePairs_2(self):
        self.assertEqual(4, Solution().reversePairs([5,4,3,2,1]))

    def test_reversePairs_3(self):
        self.assertEqual(1, Solution().reversePairs([-5,-5]))
