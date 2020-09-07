from unittest import TestCase
from problems.N1324_Print_Words_Vertically import Solution

class TestSolution(TestCase):
    def test_printVertically(self):
        self.assertListEqual(["HAY","ORO","WEU"], Solution().printVertically("HOW ARE YOU"))

    def test_printVertically_1(self):
        self.assertListEqual(["TBONTB","OEROOE","   T"], Solution().printVertically("TO BE OR NOT TO BE"))

    def test_printVertically_2(self):
        self.assertListEqual(["CIC","OSO","N M","T I","E N","S G","T"], Solution().printVertically("CONTEST IS COMING"))

