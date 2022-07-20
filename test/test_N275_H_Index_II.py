from unittest import TestCase
from problems.N275_H_Index_II import Solution

class TestSolution(TestCase):
    def test_h_index(self):
        self.assertEqual(2, Solution().hIndex([0,0,4,4]))

    def test_h_index_1(self):
        self.assertEqual(3, Solution().hIndex([0,1,3,5,6]))

    def test_h_index_2(self):
        self.assertEqual(2, Solution().hIndex([1,2,100]))

    def test_h_index_3(self):
        self.assertEqual(0, Solution().hIndex([0]))

