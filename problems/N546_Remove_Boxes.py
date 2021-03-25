from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        length = len(boxes)
        dp = [[[0] * length for _ in range(length)] for _ in range(length)]

        def dfs(l, r, k):
            if l > r:
                return 0

            if dp[l][r][k]:
                return dp[l][r][k]

            i = r
            count = k
            while i >= l and boxes[i] == boxes[r]:
                i -= 1
                count += 1
            dp[l][r][k] = dfs(l, i, 0) + count*count

            for j in range(i, l-1, -1):
                if boxes[j] != boxes[r]:
                    continue
                elif boxes[j] == boxes[j+1]:
                    continue
                dp[l][r][k] = max(dp[l][r][k], dfs(l, j, count) + dfs(j+1, i, 0))

            return dp[l][r][k]

        return dfs(0, length-1, 0)