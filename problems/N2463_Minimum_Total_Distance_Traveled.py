import sys
from typing import List

"""
Interval DP problem 

dp[i][j] : ith (index base at 0) factory cover j number of robot(index base at 1)
dist[i][j][k] : costs of ith factory cover [j, k] (all inclusive) robots 

"""
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        lr, lf = len(robot), len(factory)
        dp = [[0] * 101 for _ in range(101)]
        dp[0][0] = 0
        dist = [[[0] * 101 for _ in range(101)] for _ in range(101)]
        for i in range(lf):
            for j in range(lr):
                cur = 0
                for k in range(j, lr):
                    cur += abs(factory[i][0] - robot[k])
                    dist[i][j][k] = cur

        for j in range(1, lr + 1):
            if j <= factory[0][1]:
                dp[0][j] = dist[0][0][j-1]
            else:
                dp[0][j] = sys.maxsize

        for i in range(1, lf):
            for j in range(1, lr + 1):
                dp[i][j] = dp[i-1][j]
                for k in range(1, min(j, factory[i][1]) + 1):
                    dp[i][j] = min(dp[i][j], dp[i-1][j-k] + dist[i][j-k][j-1])

        return dp[lf-1][lr]
