from unittest import TestCase
from problems.MergeKSortedLists import ListNode, Solution

def create_link_list(numbers):
    res = l = ListNode(numbers[0])
    for n in range(1, len(numbers)):
        l.next = ListNode(numbers[n])
        l = l.next
    return res


def convert_to_list(linkList):
    res = []
    while linkList is not None:
        res.append(linkList.val)
        linkList = linkList.next
    return res

class TestSolution(TestCase):
    def test_mergeKLists(self):
        solution = Solution()
        l = []
        l.append(create_link_list([1,4,5]))
        l.append(create_link_list([1,3,4]))
        l.append(create_link_list([2,6]))
        res = solution.mergeKLists(l)
        self.assertEqual([1,1,2,3,4,4,5,6], convert_to_list(res))
