import bisect
from collections import defaultdict
from typing import List


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.map = defaultdict(list)
        self.arr = []
        for i, v in enumerate(arr):
            self.map[v].append(i)
        for k, li in self.map.items():
            self.arr.append([len(li), k])
        self.arr.sort(reverse=True)

    def query(self, left: int, right: int, threshold: int) -> int:
        for s, v in self.arr:
            if s < threshold:
                break
            li = bisect.bisect_left(self.map[v], left)
            if li == s:
                continue
            ri = bisect.bisect_right(self.map[v], right)
            if ri == 0:
                continue
            if ri - li >= threshold:
                return v
        return -1

