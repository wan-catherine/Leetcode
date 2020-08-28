from unittest import TestCase
from problems.N890_Find_And_Replace_Pattern import Solution

class TestSolution(TestCase):
    def test_findAndReplacePattern(self):
        self.assertListEqual(["mee","aqq"], Solution().findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"))

    def test_findAndReplacePattern_1(self):
        words = ["ktittgzawn", "dgphvfjniv", "gceqobzmis", "alrztxdlah", "jijuevoioe", "mawiizpkub", "onwpmnujos", "zszkptjgzj",
         "zwfvzhrucv", "isyaphcszn"]
        pattern = "zdqmjnczma"
        self.assertListEqual([], Solution().findAndReplacePattern(words, pattern))

