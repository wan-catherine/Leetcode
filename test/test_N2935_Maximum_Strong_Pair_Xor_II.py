from unittest import TestCase
from problems.N2935_Maximum_Strong_Pair_Xor_II import Solution

class TestSolution(TestCase):
    def test_maximum_strong_pair_xor(self):
        self.assertEquals(7, Solution().maximumStrongPairXor([1,2,3,4,5]))

    def test_maximum_strong_pair_xor_1(self):
        self.assertEquals(0, Solution().maximumStrongPairXor([10,100]))

    def test_maximum_strong_pair_xor_2(self):
        self.assertEquals(1020, Solution().maximumStrongPairXor([500,520,2500,3000]))
