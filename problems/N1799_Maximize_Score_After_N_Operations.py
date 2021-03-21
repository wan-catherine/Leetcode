from typing import List


class Solution:
    def maxScore_dfs(self, nums: List[int]) -> int:
        def gcd(a, b):
            while b != 0:
                a, b = b, a%b
            return a
        length = len(nums)
        gcds = {}
        for i in range(length):
            for j in range(i+1, length):
                val = gcd(nums[i],nums[j])
                gcds[(i, j)] = val
                gcds[(j, i)] = val

        memo = {}
        def dfs(round, state):
            nonlocal length
            if round > length//2:
                return 0
            if state in memo:
                return memo[state]

            ans = 0
            for i in range(length):
                for j in range(i+1, length):
                    val = (1 << i) | (1 << j)
                    if state & val:
                        continue
                    ans = max(ans, round*gcds[(i, j)] + dfs(round+1, state | val))
            memo[state] = ans
            return ans

        return dfs(1, 0)

    def maxScore(self, nums: List[int]) -> int:
        def gcd(a, b):
            while b != 0:
                a, b = b, a%b
            return a

        def get_index(state):
            x, y = None, None
            for i in range(14):
                if (state >> i) & 1:
                    if x is None:
                        x = i
                    else:
                        y = i
            return x, y

        length = len(nums)
        gcds = {}
        for i in range(length):
            for j in range(i+1, length):
                val = gcd(nums[i],nums[j])
                gcds[(i, j)] = val
                gcds[(j, i)] = val
        n = length // 2
        stateset = [[] for _ in range(n+1)]
        stateset[0].append(0)
        for i in range(1, n+1):
            state = (1 << i*2) - 1
            while state < (1 << n*2):
                stateset[i].append(state)
                c = state & (-state)
                r = state + c
                state = (((r ^ state) >> 2) // c) | r

        dp = [0] * (2**length)
        for i in range(1, n+1):
            for state in stateset[i]:
                for substate in stateset[i-1]:
                    if state & substate != substate:
                        continue
                    x, y = get_index(state - substate)
                    dp[state] = max(dp[state], dp[substate] + i*gcds[(x, y)])
        return dp[-1]