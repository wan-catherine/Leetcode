from unittest import TestCase
from problems.N1268_Search_Suggestions_System import Solution

class TestSolution(TestCase):
    def test_suggestedProducts(self):
        products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
        searchWord = "mouse"
        output = [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
        self.assertListEqual(output, Solution().suggestedProducts(products, searchWord))

    def test_suggestedProducts_1(self):
        products = ["havana"]
        searchWord = "havana"
        output =  [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
        self.assertListEqual(output, Solution().suggestedProducts(products, searchWord))

    def test_suggestedProducts_2(self):
        products = ["bags", "baggage", "banner", "box", "cloths"]
        searchWord = "bags"
        output = [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
        self.assertListEqual(output, Solution().suggestedProducts(products, searchWord))

    def test_suggestedProducts_3(self):
        products = ["havana"]
        searchWord = "tatiana"
        output = [[],[],[],[],[],[],[]]
        self.assertListEqual(output, Solution().suggestedProducts(products, searchWord))

    def test_suggestedProducts_4(self):
        products = ["code","codephone","coddle","coddles","codes"]
        searchWord = "coddle"
        output = [["coddle","coddles","code"],["coddle","coddles","code"],["coddle","coddles","code"],["coddle","coddles"],["coddle","coddles"],["coddle","coddles"]]
        self.assertListEqual(output, Solution().suggestedProducts(products, searchWord))
