class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, temp, res):
        if not s:
            res.append(temp[:])
            return
        for i in range(1, len(s)+1):
            if self.is_parlidrome(s[:i]):
                temp.append(s[:i])
                self.dfs(s[i:], temp, res)
                temp.pop()

    def is_parlidrome(self,s):
        return s == s[::-1]