from unittest import TestCase
from problems.RotateList import Solution, ListNode

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

    def test_rotateRight(self):
        solution = Solution()
        input = self.create_link_list([0,1,2])
        res = solution.rotateRight(input, 4)
        self.assertEqual([2,0,1],self.convert_to_list(res))

    def test_rotateRight_4(self):
        solution = Solution()
        input = self.create_link_list([1,2,3,4,5])
        res = solution.rotateRight(input, 2)
        self.assertEqual([4,5,1,2,3],self.convert_to_list(res))
