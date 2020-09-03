from unittest import TestCase
from problems.N1023_Camelcase_Matching import Solution

class TestSolution(TestCase):
    def test_camelMatch(self):
        queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
        pattern = "FB"
        output = [True, False, True, True, False]
        self.assertListEqual(output, Solution().camelMatch(queries, pattern))

    def test_camelMatch_1(self):
        queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
        pattern = "FoBa"
        output = [True, False, True, False, False]
        self.assertListEqual(output, Solution().camelMatch(queries, pattern))

    def test_camelMatch_2(self):
        queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
        pattern = "FoBaT"
        output = [False, True, False, False, False]
        self.assertListEqual(output, Solution().camelMatch(queries, pattern))
