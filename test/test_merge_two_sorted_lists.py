from unittest import TestCase
from problems.MergeTwoSortedLists import Solution, ListNode

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

    def test_mergeTwoLists(self):
        solution = Solution()
        res = solution.mergeTwoLists(self.create_link_list([1,2,4]),self.create_link_list( [1,3,4]))
        self.assertEqual([1,1,2,3,4,4], self.convert_to_list(res))
