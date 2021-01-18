from unittest import TestCase
from problems.N721_Accounts_Merge import Solution

class TestSolution(TestCase):
    def test_accountsMerge(self):
        accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                    ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
        output = [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
        self.assertListEqual(output, Solution().accountsMerge(accounts))

    def test_accountsMerge_1(self):
        accounts = [["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]]
        output = [["David","David0@m.co","David1@m.co","David3@m.co","David4@m.co","David5@m.co"]]
        self.assertListEqual(output, Solution().accountsMerge(accounts))

    def test_accountsMerge_2(self):
        accounts = [["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"],
         ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"],
         ["David", "David1@m.co", "David2@m.co"]]
        output = [["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]
        self.assertListEqual(output, Solution().accountsMerge(accounts))