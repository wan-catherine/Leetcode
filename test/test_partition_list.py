from unittest import TestCase
from problems.PartitionList import ListNode, Solution

class TestPartitionList(TestCase):
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

    def test_partition(self):
        solution = Solution()
        input = self.create_link_list([1,4,3,2,5,2])
        res = solution.partition(input, 3)
        self.assertEqual([1,2,2,4,3,5], self.convert_to_list(res))
