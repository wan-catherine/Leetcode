import collections


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        count = collections.Counter(s)
        keys = []
        for key, v in count.items():
            if v >= k:
                keys.append(key)
        keys.sort(reverse=True)
        length = len(keys)
        res = ""
        def check(ss):
            if not ss:
                return True
            st = ss * k
            i = 0
            for c in s:
                if c == st[i]:
                    i += 1
                if i == len(st):
                    break
            if i < len(st):
                return False
            return True
        def dfs(cur):
            nonlocal res
            if cur and not check(cur):
                return
            if len(cur) > len(res) or (len(cur) == len(res) and cur > res):
                res = cur
            if len(cur) == 7:
                return
            for i in range(length):
                dfs(cur + keys[i])
        dfs("")
        return res



