from unittest import TestCase
from problems.N565_Array_Nesting import Solution

class TestSolution(TestCase):
    def test_arrayNesting(self):
        self.assertEqual(4, Solution().arrayNesting([5,4,0,3,1,6,2]))
