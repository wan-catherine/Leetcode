from unittest import TestCase
from problems.N725_Split_Linked_List_In_Parts import Solution
from problems.Utility import create_list_from_linklist,create_linklist_from_list, ListNode

class TestSolution(TestCase):
    def test_splitListToParts(self):
        root = create_linklist_from_list([1,2,3])
        output = [[1],[2],[3],[],[]]
        res = Solution().splitListToParts(root, 5)
        check = []
        for node in res:
            check.append(create_list_from_linklist(node))
        self.assertListEqual(output, check)

    def test_splitListToParts_1(self):
        root = create_linklist_from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        output = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
        res = Solution().splitListToParts(root, 3)
        check = []
        for node in res:
            check.append(create_list_from_linklist(node))
        self.assertListEqual(output, check)
