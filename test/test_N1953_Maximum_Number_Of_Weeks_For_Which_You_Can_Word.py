from unittest import TestCase
from problems.N1953_Maximum_Number_Of_Weeks_For_Which_You_Can_Word import Solution

class TestSolution(TestCase):
    def test_number_of_weeks(self):
        self.assertEqual(6, Solution().numberOfWeeks([1,2,3]))

    def test_number_of_weeks_1(self):
        self.assertEqual(7, Solution().numberOfWeeks([5,2,1]))
