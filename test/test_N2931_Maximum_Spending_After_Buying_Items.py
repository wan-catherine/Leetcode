from unittest import TestCase
from problems.N2931_Maximum_Spending_After_Buying_Items import Solution

class TestSolution(TestCase):
    def test_max_spending(self):
        self.assertEquals(285, Solution().maxSpending([[8,5,2],[6,4,1],[9,7,3]]))

    def test_max_spending_1(self):
        self.assertEquals(386, Solution().maxSpending([[10,8,6,4,2],[9,7,5,3,2]]))
