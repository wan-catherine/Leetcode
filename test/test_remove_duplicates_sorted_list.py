from unittest import TestCase
from problems.RemoveDuplicatesSortedList import ListNode, Solution

class TestSolution(TestCase):
    def create_link_list(self, numbers):
        res = l = ListNode(numbers[0])
        for n in range(1,len(numbers)):
            l.next = ListNode(numbers[n])
            l = l.next
        return res

    def convert_to_list(self, linkList):
        res = []
        while linkList is not None:
            res.append(linkList.val)
            linkList = linkList.next
        return res

    def test_deleteDuplicates(self):
        solution = Solution()
        input = self.create_link_list([1,1,2])
        res = solution.deleteDuplicates(input)
        self.assertEqual(self.convert_to_list(res), [1,2])

    def test_deleteDuplicates_1(self):
        solution = Solution()
        input = self.create_link_list([1,1,2,3,3])
        res = solution.deleteDuplicates(input)
        self.assertEqual(self.convert_to_list(res),[1,2,3])
