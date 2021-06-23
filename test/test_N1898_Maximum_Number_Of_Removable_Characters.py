from unittest import TestCase
from problems.N1898_Maximum_Number_Of_Removable_Characters import Solution

class TestSolution(TestCase):
    def test_maximum_removals(self):
        self.assertEqual(2, Solution().maximumRemovals(s = "abcacb", p = "ab", removable = [3,1,0]))

    def test_maximum_removals_1(self):
        self.assertEqual(1, Solution().maximumRemovals(s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]))

    def test_maximum_removals_2(self):
        self.assertEqual(0, Solution().maximumRemovals(s = "abcab", p = "abc", removable = [0,1,2,3,4]))

    def test_maximum_removals_3(self):
        self.assertEqual(7, Solution().maximumRemovals("qobftgcueho", "obue", [5,3,0,6,4,9,10,7,2,8]))
