import bisect
from collections import deque


class MKAverage_TLE:
    def __init__(self, m: int, k: int):
        self.arr = []
        self.less, self.middle, self.large = [], [], []
        self.m = m
        self.k = k
        self.sum = 0

    def addElement(self, num: int) -> None:
        if len(self.arr) < self.m:
            self.arr.append(num)
            bisect.insort_left(self.middle, num)
            self.sum += num
            if len(self.arr) == self.m:
                while len(self.less) < self.k:
                    val = self.middle.pop(0)
                    bisect.insort_left(self.less, val)
                    self.sum -= val
                while len(self.large) < self.k:
                    val = self.middle.pop()
                    bisect.insort_left(self.large, val)
                    self.sum -= val
        else:
            self.arr.append(num)
            if num < self.less[-1]:
                bisect.insort_left(self.less, num)
                if len(self.less) > self.k:
                    val = self.less.pop()
                    self.middle = [val] + self.middle
                    self.sum += val
            elif num > self.large[0]:
                bisect.insort_left(self.large, num)
                if len(self.large) > self.k:
                    val = self.large.pop(0)
                    self.middle = self.middle + [val]
                    self.sum += val
            else:
                bisect.insort_left(self.middle, num)
                self.sum += num

            val = self.arr[-self.m - 1]
            if val <= self.less[-1]:
                index = bisect.bisect_left(self.less, val)
                self.less = self.less[:index] + (self.less[index + 1:] if index + 1 < len(self.less) else [])
                if len(self.less) < self.k:
                    val = self.middle.pop(0)
                    self.less.append(val)
                    self.sum -= val

            elif val >= self.large[0]:
                index = bisect.bisect_left(self.large, val)
                self.large = self.large[:index] + (self.large[index + 1:] if index + 1 < len(self.large) else [])
                if len(self.large) < self.k:
                    val = self.middle.pop()
                    self.large = [val] + self.large
                    self.sum -= val
            else:
                index = bisect.bisect_left(self.middle, val)
                self.middle = self.middle[:index] + (self.middle[index + 1:] if index + 1 < len(self.middle) else [])
                self.sum -= val

    def calculateMKAverage(self) -> int:
        if len(self.arr) < self.m:
            return -1
        return self.sum // len(self.middle)

"""
Key point: 
how to get self.result during call addElement function
"""
class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.data = deque()
        self.sorted = []
        self.result = -1

    def addElement(self, num: int) -> None:
        if len(self.data) < self.m:
            self.data.append(num)
            if len(self.data) == self.m:
                self.sorted = sorted(self.data)
                self.result = sum(self.sorted[self.k:self.m - self.k])
        else:
            idxa = bisect.bisect_left(self.sorted, num)
            if self.k <= idxa <= self.m - self.k:
                self.result += num
            elif idxa < self.k:
                self.result += self.sorted[self.k - 1]
            else:
                self.result += self.sorted[self.m - self.k]
            bisect.insort(self.sorted, num)
            self.data.append(num)
            numd = self.data.popleft()
            idxd = bisect.bisect_left(self.sorted, numd)
            if self.k <= idxd <= self.m - self.k:
                self.result -= numd
            elif idxd < self.k:
                self.result -= self.sorted[self.k]
            else:
                self.result -= self.sorted[self.m - self.k]
            self.sorted.pop(idxd)

    def calculateMKAverage(self) -> int:
        return self.result // (self.m - 2 * self.k) if self.result >= 0 else -1


obj = MKAverage(3, 1)
obj.addElement(17612)
obj.addElement(74607)
print(obj.calculateMKAverage())
obj.addElement(8272)
obj.addElement(33433)
print(obj.calculateMKAverage())
obj.addElement(15456)
obj.addElement(64938)
print(obj.calculateMKAverage())
obj.addElement(99741)
print(obj.calculateMKAverage())