import bisect
import sys
from typing import List


class Solution(object):
    def lastStoneWeightII_set(self, stones):
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
    """
    Divide all numbers into two groups,
    what is the minimum difference between the sum of two groups.
    Now it's a easy classic knapsack problem.

    Question: How is it a knapsack problem?
    My understanding of Knapsack problem is this-
    You are given a set of items , for each of which we have a weight w[i] and value v[i].
    Now we have a bag for capacity W and we maximize our profit.
    Answer:
    w[i] = stones[i]
    v[i] = stones[i]
    W = sum(stones) / 2
    """
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        half = (total+1)//2
        dp = [0] * (half + 1)
        length = len(stones)
        for i in range(length):
            for j in range(half, -1, -1):
                if j >= stones[i]:
                    dp[j] = max(dp[j], dp[j-stones[i]] + stones[i])
        return abs(total - dp[-1] * 2)
