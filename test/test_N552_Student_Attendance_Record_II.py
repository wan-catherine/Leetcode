from unittest import TestCase
from problems.N552_Student_Attendance_Record_II import Solution

class TestSolution(TestCase):
    def test_check_record(self):
        self.assertEqual(8, Solution().checkRecord(2))

    def test_check_record_1(self):
        self.assertEqual(3, Solution().checkRecord(1))

    def test_check_record_2(self):
        self.assertEqual(183236316, Solution().checkRecord(10101))
