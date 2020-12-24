from unittest import TestCase
from problems.SwapNodesPairs import Solution, ListNode


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
    def test_swapPairs(self):
        solution = Solution()
        res = solution.swapPairs(create_link_list([1,2,3,4]))
        self.assertEqual([2,1,4,3], convert_to_list(res))

    def test_swapPairs_1(self):
        solution = Solution()
        res = solution.swapPairs(None)
        self.assertEqual(None, res)

    def test_swapPairs_2(self):
        solution = Solution()
        res = solution.swapPairs(create_link_list([1,2,3]))
        self.assertEqual([2,1,3], convert_to_list(res))

