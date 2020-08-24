from unittest import TestCase
from problems.N722_Remove_Comments import Solution

class TestSolution(TestCase):
    def test_removeComments(self):
        source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;",
                  "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
        self.assertListEqual(["int main()","{ ","  ","int a, b, c;","a = b + c;","}"], Solution().removeComments(source))

    def test_removeComments_1(self):
        source = ["a/*comment", "line", "more_comment*/b"]
        self.assertListEqual(["ab"], Solution().removeComments(source))

    def test_removeComments_2(self):
        source = ["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"]
        self.assertListEqual(["struct Node{","    ","    int size;","    int val;","};"], Solution().removeComments(source))

    def test_removeComments_3(self):
        source = ["a//*b//*c","blank","d/*/e*//f"]
        self.assertListEqual(["a","blank","d/f"], Solution().removeComments(source))

    def test_removeComments_4(self):
        source = ["a/*/b//*c","blank","d//*e/*/f"]
        self.assertListEqual(["af"], Solution().removeComments(source))

    def test_removeComments_5(self):
        source = ["a/*/b//*c","blank","d/*/e*//f"]
        self.assertListEqual(["ae*"], Solution().removeComments(source))
