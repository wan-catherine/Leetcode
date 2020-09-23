from unittest import TestCase
from problems.N1105_Filling_Bookcase_Shelves import Solution

class TestSolution(TestCase):
    def test_minHeightShelves(self):
        self.assertEqual(6, Solution().minHeightShelves(books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4))

    def test_minHeightShelves_1(self):
        self.assertEqual(15, Solution().minHeightShelves([[7,3],[8,7],[2,7],[2,5]], 10))
