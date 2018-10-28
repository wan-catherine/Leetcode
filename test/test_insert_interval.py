from unittest import TestCase
from problems.InsertInterval import Solution,Interval

class TestSolution(TestCase):
    def test_insert(self):
        solution = Solution()
        res = solution.insert([Interval(1,3), Interval(6,9)], Interval(2,5))
        self.assertEqual(2, len(res))
        self.assertEqual(res[0].start, 1)
        self.assertEqual(res[0].end, 5)
        self.assertEqual(res[1].start, 6)
        self.assertEqual(res[1].end, 9)

    def test_insert_one(self):
        solution = Solution()
        res = solution.insert([Interval(1,2), Interval(3,5), Interval(6,7),Interval(8,10), Interval(12,16)], Interval(4,8))
        self.assertEqual(3, len(res))
        self.assertEqual(res[0].start, 1)
        self.assertEqual(res[0].end, 2)
        self.assertEqual(res[1].start, 3)
        self.assertEqual(res[1].end, 10)
        self.assertEqual(res[2].start, 12)
        self.assertEqual(res[2].end, 16)

    def test_insert_two(self):
        solution = Solution()
        res = solution.insert([], Interval(5,7))
        self.assertEqual(1, len(res))
        self.assertEqual(res[0].start, 5)
        self.assertEqual(res[0].end, 7)

    def test_insert_three(self):
        solution = Solution()
        res = solution.insert([Interval(1,5)], Interval(2,7))
        self.assertEqual(1, len(res))
        self.assertEqual(res[0].start, 1)
        self.assertEqual(res[0].end, 7)