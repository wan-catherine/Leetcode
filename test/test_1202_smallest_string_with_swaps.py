from unittest import TestCase
from problems.N1202_Smallest_String_With_Swaps import Solution

class TestSolution(TestCase):
    def test_smallestStringWithSwaps(self):
        s = "dcab"
        pairs = [[0, 3], [1, 2]]
        self.assertEqual("bacd", Solution().smallestStringWithSwaps(s,pairs))

    def test_smallestStringWithSwaps_1(self):
        s = "dcab"
        pairs = [[0, 3], [1, 2], [0, 2]]
        self.assertEqual("abcd", Solution().smallestStringWithSwaps(s,pairs))

    def test_smallestStringWithSwaps_2(self):
        s = "cba"
        pairs = [[0, 1], [1, 2]]
        self.assertEqual("abc", Solution().smallestStringWithSwaps(s,pairs))

    def test_smallestStringWithSwaps_3(self):
        s = "udyyek"
        pairs = [[3, 3], [3, 0], [5, 1], [3, 1], [3, 4], [3, 5]]
        self.assertEqual("deykuy", Solution().smallestStringWithSwaps(s,pairs))

    def test_smallestStringWithSwaps_4(self):
        s = "xwwbesrhlaoucciymqe"
        pairs = [[12, 5], [17, 8], [0, 8], [8, 13], [16, 10], [4, 15], [11, 12], [2, 11], [14, 7], [13, 18], [1, 10], [4, 8],
         [2, 17], [8, 1], [15, 13], [16, 12], [16, 18], [13, 11], [12, 0]]
        self.assertEqual("ccebelrhmaoqsuiwwxy", Solution().smallestStringWithSwaps(s,pairs))
