from unittest import TestCase
from problems.N1054_Distant_Barcodes import Solution

class TestSolution(TestCase):
    def test_rearrangeBarcodes(self):
        self.assertListEqual([2,1,2,1,2,1], Solution().rearrangeBarcodes([1,1,1,2,2,2]))

    def test_rearrangeBarcodes_1(self):
        self.assertListEqual([1,3,1,3,2,1,2,1], Solution().rearrangeBarcodes([1,1,1,1,2,2,3,3]))
