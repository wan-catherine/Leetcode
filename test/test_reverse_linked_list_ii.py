from unittest import TestCase
from problems.ReverseLinkedListII import Solution, ListNode

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

    def test_reverseBetween(self):
        solution = Solution()
        res = solution.reverseBetween(self.create_link_list([1,2,3,4,5]), 2, 4)
        self.assertEqual(self.convert_to_list(res), [1,4,3,2,5])

    def test_reverseBetween_two(self):
        solution = Solution()
        res = solution.reverseBetween(self.create_link_list([3,5]), 1, 1)
        self.assertEqual(self.convert_to_list(res), [3,5])

    def test_reverseBetween_two(self):
        solution = Solution()
        res = solution.reverseBetween(self.create_link_list([3,5]), 1, 2)
        self.assertEqual(self.convert_to_list(res), [5,3])

    def test_reverseBetween_three(self):
        solution = Solution()
        res = solution.reverseBetween(self.create_link_list([1,2,3]), 1, 2)
        self.assertEqual(self.convert_to_list(res), [2,1,3])