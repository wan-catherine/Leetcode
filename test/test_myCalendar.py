from unittest import TestCase
from problems.N729_My_Calendar_I import MyCalendar

class TestMyCalendar(TestCase):
    def test_book(self):
        obj = MyCalendar()
        input = [[37,50],[33,50],[4,17],[35,48],[8,25]]
        res = []
        for li in input:
            res.append(obj.book(*li))
        self.assertListEqual([True,False,True,False,False], res)
