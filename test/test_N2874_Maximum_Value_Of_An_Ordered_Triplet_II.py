from unittest import TestCase
from problems.N2874_Maximum_Value_Of_An_Ordered_Triplet_II import Solution

class TestSolution(TestCase):
    def test_maximum_triplet_value(self):
        self.assertEquals(77, Solution().maximumTripletValue([12,6,1,2,7]))

    def test_maximum_triplet_value_1(self):
        self.assertEquals(133, Solution().maximumTripletValue([1,10,3,4,19]))

    def test_maximum_triplet_value_2(self):
        self.assertEquals(0, Solution().maximumTripletValue([1,2,3]))
