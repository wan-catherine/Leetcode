from unittest import TestCase
from problems.N1169_Invalid_Transactions import Solution

class TestSolution(TestCase):
    def test_invalidTransactions(self):
        transactions = ["alice,20,800,mtv", "alice,50,100,beijing"]
        self.assertListEqual(["alice,20,800,mtv","alice,50,100,beijing"], Solution().invalidTransactions(transactions))

    def test_invalidTransactions_1(self):
        transactions = ["alice,20,800,mtv", "alice,50,1200,mtv"]
        self.assertListEqual(["alice,50,1200,mtv"], Solution().invalidTransactions(transactions))

    def test_invalidTransactions_2(self):
        transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
        self.assertListEqual(["bob,50,1200,mtv"], Solution().invalidTransactions(transactions))

    def test_invalidTransactions_3(self):
        transactions = ["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]
        self.assertListEqual(["bob,689,1910,barcelona","bob,832,1726,barcelona","bob,820,596,bangkok"], Solution().invalidTransactions(transactions))
