from unittest import TestCase
from problems.N636_Exclusive_Time_Of_Functions import Solution

class TestSolution(TestCase):
    def test_exclusiveTime(self):
        self.assertListEqual([3,4], Solution().exclusiveTime(n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]))

    def test_exclusiveTime_1(self):
        self.assertListEqual([8], Solution().exclusiveTime(n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))

    def test_exclusiveTime_2(self):
        self.assertListEqual([7,1], Solution().exclusiveTime(n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))

    def test_exclusiveTime_3(self):
        self.assertListEqual([8,1], Solution().exclusiveTime(n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]))

    def test_exclusiveTime_4(self):
        self.assertListEqual([1], Solution().exclusiveTime(n = 1, logs = ["0:start:0","0:end:0"]))

    def test_exclusiveTime_5(self):
        self.assertListEqual([6], Solution().exclusiveTime(1, ["0:start:0","0:start:1","0:start:2","0:end:3","0:end:4","0:end:5"]))