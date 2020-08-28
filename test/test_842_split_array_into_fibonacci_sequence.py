from unittest import TestCase
from problems.N842_Split_Array_Into_Fibonacci_Sequence import Solution

class TestSolution(TestCase):
    def test_splitIntoFibonacci(self):
        self.assertListEqual([123,456,579], Solution().splitIntoFibonacci("123456579"))

    def test_splitIntoFibonacci_1(self):
        self.assertListEqual([1,1,2,3,5,8,13], Solution().splitIntoFibonacci("11235813"))

    def test_splitIntoFibonacci_2(self):
        self.assertListEqual([], Solution().splitIntoFibonacci("112358130"))

    def test_splitIntoFibonacci_3(self):
        self.assertListEqual([], Solution().splitIntoFibonacci("0123"))

    def test_splitIntoFibonacci_4(self):
        self.assertListEqual([110, 1, 111], Solution().splitIntoFibonacci("1101111"))

    def test_splitIntoFibonacci_5(self):
        self.assertListEqual([], Solution().splitIntoFibonacci("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"))

    def test_splitIntoFibonacci_6(self):
        self.assertListEqual([], Solution().splitIntoFibonacci("3611537383985343591834441270352104793375145479938855071433500231900737525076071514982402115895535257195564161509167334647108949738176284385285234123461518508746752631120827113919550237703163294909"))
