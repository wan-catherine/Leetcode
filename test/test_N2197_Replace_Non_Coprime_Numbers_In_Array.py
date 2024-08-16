from unittest import TestCase
from problems.N2197_Replace_Non_Coprime_Numbers_In_Array import Solution

class TestSolution(TestCase):
    def test_replace_non_coprimes(self):
        self.assertListEqual([12,7,6], Solution().replaceNonCoprimes([6,4,3,2,7,6,2]))

    def test_replace_non_coprimes_1(self):
        self.assertListEqual([2,1,1,3], Solution().replaceNonCoprimes([2,2,1,1,3,3,3]))

    def test_replace_non_coprimes_2(self):
        self.assertListEqual([2009,20677,825], Solution().replaceNonCoprimes([287,41,49,287,899,23,23,20677,5,825]))
