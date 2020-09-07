from unittest import TestCase
from problems.N1410_HTML_Entity_Parser import Solution

class TestSolution(TestCase):
    def test_entityParser(self):
        self.assertEqual("& is an HTML entity but &ambassador; is not.", Solution().entityParser("&amp; is an HTML entity but &ambassador; is not."))

    def test_entityParser_1(self):
        self.assertEqual("and I quote: \"...\"", Solution().entityParser("and I quote: &quot;...&quot;"))

    def test_entityParser_2(self):
        self.assertEqual("Stay home! Practice on Leetcode :)", Solution().entityParser("Stay home! Practice on Leetcode :)"))

    def test_entityParser_3(self):
        self.assertEqual("x > y && x < y is always false", Solution().entityParser("x &gt; y &amp;&amp; x &lt; y is always false"))

    def test_entityParser_4(self):
        self.assertEqual("leetcode.com/problemset/all", Solution().entityParser("leetcode.com&frasl;problemset&frasl;all"))

    def test_entityParser_5(self):
        self.assertEqual("&gt;", Solution().entityParser("&amp;gt;"))