"""
For the first try, I didn't use memo, so there might be a lot of duplicated cases.
"""
from typing import List


class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones[1] != 1:
            return False
        if len(stones) == 2:
            return True
        mapping = set(stones)
        last = stones[-1]
        queue = set()
        queue.add((1,1))
        memo = set()
        memo.add((1,1))
        while queue:
            new_queue= set()
            for pos, k in queue:
                addone, same, subone = pos + k + 1, pos + k, pos + k - 1
                if (addone, k+1) not in memo and addone in mapping:
                    if addone == last:
                        return True
                    new_queue.add((addone, k+1))
                    memo.add((addone, k + 1))
                if (same, k) not in memo and same in mapping:
                    if same == last:
                        return True
                    new_queue.add((same, k))
                    memo.add((same, k))
                if (subone,k-1) not in memo and subone in mapping:
                    if subone == last:
                        return True
                    if k - 1 > 0:
                        new_queue.add((subone,k-1))
                        memo.add((subone, k - 1))
            queue = new_queue
        return False

    def canCross_dp(self, stones: List[int]) -> bool:
        if stones[1] - stones[0] != 1:
            return False
        mapping = {stones[i]:i for i in range(len(stones))}
        memo = {}
        def helper(index, k):
            if index == len(stones) - 1:
                return True
            if (index, k) in memo:
                return memo[(index, k)]
            for i in (-1, 0, 1):
                val = stones[index] + k + i
                if val <= stones[index] or val not in mapping:
                    continue
                if helper(mapping[val], k+i):
                    return True
            memo[(index, k)] = False
            return False
        return helper(1, 1)
