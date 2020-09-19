from unittest import TestCase
from problems.N1024_Video_Stitching import Solution

class TestSolution(TestCase):
    def test_videoStitching(self):
        self.assertEqual(3, Solution().videoStitching(clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10))

    def test_videoStitching_1(self):
        self.assertEqual(-1, Solution().videoStitching(clips = [[0,1],[1,2]], T = 5))

    def test_videoStitching_2(self):
        self.assertEqual(3, Solution().videoStitching(clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9))

    def test_videoStitching_3(self):
        self.assertEqual(2, Solution().videoStitching(clips = [[0,4],[2,8]], T = 5))

    def test_videoStitching_4(self):
        self.assertEqual(-1, Solution().videoStitching([[0,2],[4,8]], 5))

    def test_videoStitching_5(self):
        self.assertEqual(1, Solution().videoStitching([[5,7],[1,8],[0,0],[2,3],[4,5],[0,6],[5,10],[7,10]], 5))

