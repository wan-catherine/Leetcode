import bisect
import sys
from typing import List


class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        packages = [0] + packages
        l = len(packages)
        prefix = packages[:]
        for i in range(1, len(packages)):
            prefix[i] += prefix[i-1]
        res = sys.maxsize
        length = len(boxes)
        for i in range(length):
            boxes[i].sort()
            if packages[-1] > boxes[i][-1]:
                continue
            ans = 0
            previous = 0
            for c in boxes[i]:
                # here we need to use bisect.bisect , not bisect.bisect_left
                # because there might be some duplicated c.
                index = bisect.bisect(packages, c)
                if index < l and packages[index] == c:
                    origin = prefix[index] - prefix[previous]
                    current = c * (index - previous)
                    previous = index
                else:
                    origin = prefix[index-1] - prefix[previous]
                    current = c * (index - previous - 1)
                    previous = index - 1
                ans += current - origin

            res = min(res, ans)
        return res % (10**9 + 7) if res < sys.maxsize else -1

