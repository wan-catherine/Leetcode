from unittest import TestCase
from problems.N1687_Delivering_Boxes_From_Storage_To_Ports import Solution

class TestSolution(TestCase):
    def test_boxDelivering(self):
        self.assertEqual(4, Solution().boxDelivering(boxes = [[1,1],[2,1],[1,1]], portsCount = 2, maxBoxes = 3, maxWeight = 3))

    def test_boxDelivering_1(self):
        self.assertEqual(6, Solution().boxDelivering(boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]], portsCount = 3, maxBoxes = 3, maxWeight = 6))

    def test_boxDelivering_2(self):
        self.assertEqual(6, Solution().boxDelivering(boxes = [[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]], portsCount = 3, maxBoxes = 6, maxWeight = 7))

    def test_boxDelivering_3(self):
        self.assertEqual(14, Solution().boxDelivering(boxes = [[2,4],[2,5],[3,1],[3,2],[3,7],[3,1],[4,4],[1,3],[5,2]], portsCount = 5, maxBoxes = 5, maxWeight = 7))
