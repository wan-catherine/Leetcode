import bisect
from typing import List


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        length = len(tasks)
        lw = len(workers)

        def check(k):
            p = pills
            if k > lw:
                return False
            wks = sorted(workers)
            for i in range(k - 1, -1, -1):
                if wks[-1] >= tasks[i]:
                    wks.pop()
                    continue
                if p == 0:
                    return False
                index = bisect.bisect_left(wks, tasks[i] - strength)
                if index == len(wks):
                    return False
                wks.pop(index)
                # if use this way , then it will be TLE.
                # wks = wks[:index] + wks[index+1:]
                p -= 1
            return True

        l, r = 0, length
        while l < r:
            mid = (r - l + 1) // 2 + l
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l