from unittest import TestCase
from problems.RemoveLinkedListElements import Solution, ListNode

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
    def test_removeElements(self):
        solution = Solution()
        head = create_link_list([1,2,6,3,4,5,6])
        res = solution.removeElements(head, 6)
        self.assertEqual(convert_to_list(res), [1,2,3,4,5])

    def test_removeElements_two(self):
        solution = Solution()
        head = create_link_list([1,2,1,3,4,5,6])
        res = solution.removeElements(head, 1)
        self.assertEqual(convert_to_list(res), [2,3,4,5,6])



