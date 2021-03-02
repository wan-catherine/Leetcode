from unittest import TestCase
from problems.N975_Odd_Even_Jump import Solution

class TestSolution(TestCase):
    def test_oddEvenJumps(self):
        self.assertEqual(2, Solution().oddEvenJumps([10,13,12,14,15]))

    def test_oddEvenJumps_1(self):
        self.assertEqual(3, Solution().oddEvenJumps([2,3,1,1,4]))

    def test_oddEvenJumps_2(self):
        self.assertEqual(3, Solution().oddEvenJumps([5,1,3,4,2]))

    def test_oddEvenJumps_3(self):
        self.assertEqual(6, Solution().oddEvenJumps([1,2,3,2,1,4,4,5]))

    def test_oddEvenJumps_4(self):
        self.assertEqual(21, Solution().oddEvenJumps([31,28,8,41,20,28,41,26,46,30,41,34,2,29,24,39,28,11,22,21,33,15,14,35,49,23,15,46,19,28,13,19,38]))