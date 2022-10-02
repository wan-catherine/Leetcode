class Solution:
    def deleteString(self, s: str) -> int:
        if len(set(s)) == 1:
            return len(s)
        memo = {}
        def dfs(cur):
            if cur in memo:
                return memo[cur]
            length = len(cur)
            ans = 1
            for i in range(1, length//2+1):
                if cur[:i] == cur[i:2*i]:
                    ans = max(ans, dfs(cur[i:]) + 1)
            memo[cur] = ans
            return ans
        return dfs(s)