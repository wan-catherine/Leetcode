from unittest import TestCase
from problems.N609_Find_Duplicate_File_In_System import Solution

class TestSolution(TestCase):
    def test_findDuplicate(self):
        input = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
        output = [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
        self.assertListEqual(output, Solution().findDuplicate(input))
