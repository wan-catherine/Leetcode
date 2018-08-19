from unittest import TestCase
from problems.RemoveNthNodeFromEndList import Solution, ListNode

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

    def test_removeNthFromEnd(self):
        solution = Solution()
        head =  ListNode(1)
        res = solution.removeNthFromEnd(head, 1)
        self.assertEqual(res , None)

    def test_removeNthFromEnd_two(self):
        solution = Solution()
        res = solution.removeNthFromEnd(self.create_link_list([1,2,3,4,5]), 2)
        self.assertEqual([1,2,3,5], self.convert_to_list(res))

    def test_removeNthFromEnd_end(self):
        solution = Solution()
        res = solution.removeNthFromEnd(self.create_link_list([1,2,3,4,5]), 1)
        self.assertEqual([1,2,3,4], self.convert_to_list(res))

    def test_removeNthFromEnd_first(self):
        solution = Solution()
        res = solution.removeNthFromEnd(self.create_link_list([1,2,3,4,5]), 5)
        self.assertEqual([2,3,4,5], self.convert_to_list(res))

    def test_removeNthFromEnd_1(self):
        solution = Solution()
        res = solution.removeNthFromEnd(self.create_link_list([1,2]), 1)
        self.assertEqual([1], self.convert_to_list(res))
