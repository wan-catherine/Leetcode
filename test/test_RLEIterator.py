from unittest import TestCase
from problems.N900_RLE_Iterator import RLEIterator

class TestRLEIterator(TestCase):
    def test_next(self):
        rle = RLEIterator([3,8,0,9,2,5])
        next = [2,1,1,2]
        res = []
        for i in next:
            res.append(rle.next(i))
        self.assertListEqual([8,8,5,-1], res)

    def test_next_1(self):
        rle = RLEIterator([784, 303, 477, 583, 909, 505])
        next = [130, 333, 238, 87, 301, 276]
        res = []
        for i in next:
            res.append(rle.next(i))
        self.assertListEqual([303,303,303,583,583,505], res)
