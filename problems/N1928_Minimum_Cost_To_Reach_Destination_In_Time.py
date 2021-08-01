import collections
import sys
from typing import List


class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        graph = collections.defaultdict(list)
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))
        length = len(passingFees)
        dp = [[sys.maxsize] * (maxTime + 1) for _ in range(length)]
        dp[0][0] = passingFees[0]
        stack = [(0, 0)]
        previous = [[maxTime, sys.maxsize] for _ in range(length)]
        # when for same city, if the time and fees already more than previous, then we don't need to consider it.
        previous[0] = [0, passingFees[0]]
        while stack:
            new_stack = []
            for idx, time in stack:
                for nxt, t in graph[idx]:
                    if time + t > maxTime:
                        continue
                    if dp[nxt][time+t] > dp[idx][time] + passingFees[nxt]:
                        dp[nxt][time + t] = dp[idx][time] + passingFees[nxt]
                        if time + t < previous[nxt][0] or dp[nxt][time + t] < previous[nxt][1]:
                            new_stack.append((nxt, time + t))
                            previous[nxt] = [time+t, dp[nxt][time + t]]
            stack = new_stack
        res = min(dp[length-1])
        return res if res != sys.maxsize else -1