import bisect
import sys


class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        length = len(stones)
        if length == 1:
            return stones[0]
        sums = set()
        sums.add(stones[0])
        for i in range(1, length):
            new_sums = set()
            ans = sys.maxsize
            for s in sums:
                new_sums.add(s + stones[i])
                ans = min(ans, abs(s+stones[i]))
                new_sums.add(s - stones[i])
                ans = min(ans, abs(s-stones[i]))
            sums = new_sums
        # print(sums)
        return ans

