from unittest import TestCase
from problems.N752_Open_The_Lock import Solution

class TestSolution(TestCase):
    def test_openLock(self):
        self.assertEqual(6, Solution().openLock(["0201","0101","0102","1212","2002"], target = "0202"))

    def test_openLock_1(self):
        self.assertEqual(1, Solution().openLock(["8888"], target = "0009"))

    def test_openLock_2(self):
        self.assertEqual(-1, Solution().openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"))

    def test_openLock_3(self):
        self.assertEqual(-1, Solution().openLock(["0000"], target = "8888"))

    def test_openLock_4(self):
        self.assertEqual(0, Solution().openLock(["0201","0101","0102","1212","2002"], "0000"))