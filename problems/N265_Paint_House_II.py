import sys
"""
265. Paint House II
There are a row of n houses, each house can be painted with one of the k colors. 
The cost of painting each house with a certain color is different. 
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix.
For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... 
Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
Follow up:
Could you solve it in O(nk) runtime?
"""

class Solution:
    def minCostII(self, costs) -> int:
        if not costs or not costs[0]:
            return 0
        rows, cols = len(costs), len(costs[0])
        dp = [[0] * cols for _ in range(rows)]
        first, second = (sys.maxsize, -1), (sys.maxsize, -1)
        for i in range(cols):
            dp[0][i] = costs[0][i]
            if costs[0][i] < first[0]:
                second = first
                first = costs[0][i], i
            elif costs[0][i] < second[0]:
                second = costs[0][i], i

        for i in range(1, rows):
            pf, ps = first, second
            first, second = (sys.maxsize, -1), (sys.maxsize, -1)
            print(dp[i-1])
            for j in range(cols):
                if j == pf[1]:
                    dp[i][j] = costs[i][j] + ps[0]
                else:
                    dp[i][j] = costs[i][j] + pf[0]
                if dp[i][j] < first[0]:
                    # this is a key part !!!
                    second = first
                    first = dp[i][j], j
                elif dp[i][j] < second[0]:
                    second = dp[i][j], j

        return min(dp[-1])