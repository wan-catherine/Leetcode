from unittest import TestCase
from problems.N1471_The_K_Strongest_Values_In_An_Array import Solution

class TestSolution(TestCase):
    def test_getStrongest(self):
        self.assertListEqual([5,1], Solution().getStrongest([1,2,3,4,5], 2))

    def test_getStrongest_1(self):
        self.assertListEqual([5,5], Solution().getStrongest([1,1,3,5,5], 2))

    def test_getStrongest_2(self):
        self.assertListEqual([11,8,6,6,7], Solution().getStrongest([6,7,11,7,6,8], 5))

    def test_getStrongest_3(self):
        self.assertListEqual([-3,11,2], Solution().getStrongest([6,-3,7,2,11], 3))

    def test_getStrongest_4(self):
        self.assertListEqual([22,17], Solution().getStrongest([-7,22,17,3], 2))

    def test_getStrongest_5(self):
        self.assertListEqual([777,240,101,80,-996,-798,-698], Solution().getStrongest([-698, 240, 80, -509, -996, -798, 777, 101], 7))

    def test_getStrongest_6(self):
        self.assertListEqual([598,521,-918,-532,-493,-76,-262], Solution().getStrongest([-493, 598, -262, -918, -76, -532, 521], 7))