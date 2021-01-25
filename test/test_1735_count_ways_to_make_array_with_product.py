from unittest import TestCase
from problems.N1735_Count_Ways_To_Make_Array_With_Product import Solution

class TestSolution(TestCase):
    def test_waysToFillArray(self):
        self.assertListEqual([4,1,50734910], Solution().waysToFillArray([[2,6],[5,1],[73,660]]))

    def test_waysToFillArray_1(self):
        self.assertListEqual([1,2,3,10,5], Solution().waysToFillArray([[1,1],[2,2],[3,3],[4,4],[5,5]]))

    def test_waysToFillArray_2(self):
        self.assertListEqual([865201973,101,466,308,411805778], Solution().waysToFillArray([[373,196],[101,229],[466,109],[308,83],[296,432]]))
