from unittest import TestCase
from problems.N68_Text_Justification import Solution

class TestSolution(TestCase):
    def test_full_justify(self):
        self.assertListEqual(["This    is    an","example  of text","justification.  "], Solution().fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16))

    def test_full_justify_1(self):
        self.assertListEqual([
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
], Solution().fullJustify(words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16))

    def test_full_justify_2(self):
        self.assertListEqual([
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
], Solution().fullJustify(words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20))
