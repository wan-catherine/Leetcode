class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        sub = set()
        def dfs(str):
            if not str:
                return len(sub)
            count = 0
            for i in range(1, len(str) + 1):
                if str[:i] in sub:
                    continue
                sub.add(str[:i])
                count = max(count, dfs(str[i:]))
                sub.remove(str[:i])
            return count
        return dfs(s)



