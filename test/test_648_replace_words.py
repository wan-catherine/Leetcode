from unittest import TestCase
from problems.N648_Replace_Words import Solution

class TestSolution(TestCase):
    def test_replaceWords(self):
        dict = ["cat", "bat", "rat"]
        sentence = "the cattle was rattled by the battery"
        self.assertEqual("the cat was rat by the bat", Solution().replaceWords(dict, sentence))
