class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        length = len(s)
        res = set()
        ans = '9'*length
        def dfs(cur):
            nonlocal ans
            temp = [int(i) for i in cur]
            for i in range(1, length, 2):
                temp[i] = (temp[i] + a) % 10
            new_s = ''.join(map(str, temp))
            if new_s not in res:
                res.add(new_s)
                ans = min(ans, new_s)
                dfs(new_s)
            new_s = ''.join(map(str, cur[-b:] + cur[:-b]))
            if new_s not in res:
                res.add(new_s)
                ans = min(ans, new_s)
                dfs(new_s)
        dfs(s)
        return ans




