import bisect


class CountIntervals:

    def __init__(self):
        self.intervals = []
        self.res = 0

    def add(self, left: int, right: int) -> None:
        start, end = left, right
        l = bisect.bisect_left(self.intervals, [left, left])
        if l > 0 and self.intervals[l-1][1] >= left:
            start = min(self.intervals[l-1][0], start)
            l -= 1
        r = bisect.bisect_left(self.intervals, [right, right])
        if r < len(self.intervals) and self.intervals[r][0] == right:
            end = self.intervals[r][1]
            r += 1
        elif r > 0:
            end = max(self.intervals[r-1][1], end)
        index = l
        while index < r:
            self.res -= self.intervals[index][1] - self.intervals[index][0] + 1
            index += 1
        self.intervals[l:r] = [[start, end]]
        self.res += end - start + 1

    def count(self) -> int:
        return self.res

# Your CountIntervals object will be instantiated and called as such:
obj = CountIntervals()
obj.add(5,10)
obj.add(3, 5)
param_2 = obj.count()
print(param_2)