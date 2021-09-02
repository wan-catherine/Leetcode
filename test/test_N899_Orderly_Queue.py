from unittest import TestCase
from problems.N899_Orderly_Queue import Solution

class TestSolution(TestCase):
    def test_orderly_queue(self):
        self.assertEqual("acb", Solution().orderlyQueue(s = "cba", k = 1))

    def test_orderly_queue_1(self):
        self.assertEqual("aaabc", Solution().orderlyQueue(s = "baaca", k = 3))
