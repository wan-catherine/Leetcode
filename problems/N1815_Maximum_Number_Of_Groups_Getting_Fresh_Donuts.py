from typing import List


class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        batches = [0] * batchSize
        res = 0
        for g in groups:
            if not g%batchSize:
                res += 1
                continue
            batches[g%batchSize] += 1
        memo = {}

        def dfs(state, left):
            if state in memo:
                return memo[state]
            ans = 0
            arr = list(state)
            for i in range(batchSize):
                if not state[i]:
                    continue
                arr[i] -= 1
                ans = max(ans, dfs(tuple(arr), (left + i) % batchSize) + (1 if left == 0 else 0))
                arr[i] += 1
            memo[state] = ans
            return ans

        return res + dfs(tuple(batches), 0)
