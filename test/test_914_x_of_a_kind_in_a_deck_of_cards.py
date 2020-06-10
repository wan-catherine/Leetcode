from unittest import TestCase
from problems.N914_X_Of_A_Kind_In_A_Deck_Of_Cards import Solution

class TestSolution(TestCase):
    def test_hasGroupsSizeX(self):
        self.assertTrue(Solution().hasGroupsSizeX([1,2,3,4,4,3,2,1]))

    def test_hasGroupsSizeX_1(self):
        self.assertFalse(Solution().hasGroupsSizeX([1,1,1,2,2,2,3,3]))

    def test_hasGroupsSizeX_2(self):
        self.assertFalse(Solution().hasGroupsSizeX([1]))

    def test_hasGroupsSizeX_3(self):
        self.assertTrue(Solution().hasGroupsSizeX([1,1]))

    def test_hasGroupsSizeX_4(self):
        self.assertTrue(Solution().hasGroupsSizeX([1,1,2,2,2,2]))
