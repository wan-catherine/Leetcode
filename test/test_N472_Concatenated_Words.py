from unittest import TestCase
from problems.N472_Concatenated_Words import Solution

class TestSolution(TestCase):
    def test_find_all_concatenated_words_in_adict(self):
        self.assertListEqual(["catsdogcats","dogcatsdog","ratcatdogcat"], Solution().findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))

    def test_find_all_concatenated_words_in_adict_1(self):
        self.assertListEqual(["catdog"], Solution().findAllConcatenatedWordsInADict(["cat","dog","catdog"]))

