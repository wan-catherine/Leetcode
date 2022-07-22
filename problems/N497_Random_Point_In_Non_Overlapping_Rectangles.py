import bisect
import random
from typing import List

"""
Be careful for bisect.bisect
"""

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.length = len(rects)
        self.counts = [0] * (self.length + 1)
        for i in range(self.length):
            x1, y1, x2, y2 = self.rects[i]
            self.counts[i + 1] = (x2 - x1 + 1) * (y2 - y1 + 1) + self.counts[i]

        # self.counts, sum = [], 0
        # for i in range(self.length):
        #     x1, y1, x2, y2 = self.rects[i]
        #     self.counts.append((x2 - x1 + 1) * (y2 - y1 + 1) + sum)
        #     sum = self.counts[-1]

    def pick(self) -> List[int]:
        index = self.get_index() - 1 #need to minor one here , becasue self.counts is (self.length + 1)
        x1, y1, x2, y2 = self.rects[index]
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        return [x, y]

    def get_index(self):
        target = random.randint(0, self.counts[-1])
        # print(target)
        left, right = 0, self.length
        while left < right:
            index = (right - left) // 2 + left
            val = self.counts[index]
            if val == target:
                return index
            if val < target:
                left = index + 1
            else:
                right = index
        # print(left)
        return left

    def pick_biset(self) -> List[int]:
        # here mush use: self.counts[-1] - 1
        # bisect.bisect search the position which is rightest.
        # if we use self.counts[-1], here , the bisect.bisect will return self.length
        target = random.randint(0, self.counts[-1] - 1)
        index = bisect.bisect(self.counts, target)
        x1, y1, x2, y2 = self.rects[index-1]
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()