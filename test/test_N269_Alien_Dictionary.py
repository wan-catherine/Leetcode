from unittest import TestCase
from problems.N269_Alien_Dictionary import Solution

class TestSolution(TestCase):
    def test_alien_order(self):
        self.assertEqual("wertf", Solution().alienOrder(["wrt","wrf","er","ett","rftt"]))

    def test_alien_order_1(self):
        self.assertEqual("zx", Solution().alienOrder(["z","x"]))

    def test_alien_order_2(self):
        self.assertEqual("", Solution().alienOrder(["z","x","z"]))

    def test_alien_order_3(self):
        self.assertEqual("z", Solution().alienOrder(["z","z"]))

    def test_alien_order_4(self):
        self.assertEqual("caz", Solution().alienOrder(["az", "azc"]))

    def test_alien_order_5(self):
        self.assertEqual("yzx", Solution().alienOrder(["zy","zx"]))

    def test_alien_order_6(self):
        self.assertEqual("cabz", Solution().alienOrder(["ac","ab","zc","zb"]))