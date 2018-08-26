from unittest import TestCase
from problems.ReverseNodesKGroup import Solution, ListNode


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
    def test_reverseKGroup(self):
        solution = Solution()
        res = solution.reverseKGroup(create_link_list([1,2,3,4,5]), 2)
        self.assertEqual([2,1,4,3,5], convert_to_list(res))

    def test_reverseKGroup_three(self):
        solution = Solution()
        res = solution.reverseKGroup(create_link_list([1, 2, 3, 4, 5]), 3)
        self.assertEqual([3,2,1,4,5], convert_to_list(res))

    def test_reverseKGroup_five(self):
        solution = Solution()
        res = solution.reverseKGroup(create_link_list([1, 2, 3, 4, 5]), 5)
        self.assertEqual([5,4,3,2,1], convert_to_list(res))

    def test_reverseKGroup_empty(self):
        solution = Solution()
        res = solution.reverseKGroup(None, 5)
        self.assertEqual([], convert_to_list(res))