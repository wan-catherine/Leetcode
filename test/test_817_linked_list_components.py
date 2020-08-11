from unittest import TestCase
from problems.Utility import create_list_from_linklist,create_linklist_from_list
from problems.N817_Linked_List_Components import Solution

class TestSolution(TestCase):
    def test_numComponents(self):
        head = create_linklist_from_list([0,1,2,3])
        G = [0, 1, 3]
        self.assertEqual(2, Solution().numComponents(head, G))

    def test_numComponents_1(self):
        head = create_linklist_from_list([0,1,2,3,4])
        G = [0, 3, 1, 4]
        self.assertEqual(2, Solution().numComponents(head, G))

    def test_numComponents_2(self):
        head = create_linklist_from_list([0, 1, 2])
        G = [1, 0]
        self.assertEqual(1, Solution().numComponents(head, G))

