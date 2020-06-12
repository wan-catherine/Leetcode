from unittest import TestCase
from problems.N1299_Replace_Elements_With_Greatest_Element_On_Right_Side import Solution

class TestSolution(TestCase):
    def test_replaceElements(self):
        self.assertListEqual([18,6,6,6,1,-1], Solution().replaceElements([17,18,5,4,6,1]))
