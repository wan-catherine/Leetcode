from unittest import TestCase
from problems.AddTwoNumbers import ListNode, Solution

class TestAddTwoNumbers(TestCase):
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

    def test_add_two_numbers_with_same_long_numbers(self):
        l1 = self.create_link_list([2,4,3])
        l2 = self.create_link_list([5,6,4])
        solution = Solution()
        res = solution.addTwoNumbers(l1,l2)
        self.assertListEqual([7,0,8], self.convert_to_list(res))

    def test_add_two_numbers_with_two_zero(self):
        l1 = self.create_link_list([0])
        l2 = self.create_link_list([0])
        solution = Solution()
        res = solution.addTwoNumbers(l1,l2)
        self.assertListEqual([0], self.convert_to_list(res))

    def test_add_two_numbers_with_different_long_numbers(self):
        l1 = self.create_link_list([9,9])
        l2 = self.create_link_list([9,9,9])
        solution = Solution()
        res = solution.addTwoNumbers(l1,l2)
        self.assertListEqual([8,9,0,1], self.convert_to_list(res))
