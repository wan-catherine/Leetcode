import collections
from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        target = list(target)
        ls, lt = len(stamp), len(target)

        def helper(arr):
            nonlocal ls
            res = 0
            for i in range(ls):
                if arr[i] == '*':
                    continue
                if arr[i] == stamp[i]:
                    res += 1
                else:
                    return 0
            return res

        matches, res = 0, []
        while matches < lt:
            count = matches
            for i in range(lt - ls + 1):
                cur = helper(target[i:i+ls])
                if cur:
                    matches += cur
                    target[i:i+ls] = ['*']*ls
                    res.append(i)
            if matches == count:
                return []
        return res[::-1]


