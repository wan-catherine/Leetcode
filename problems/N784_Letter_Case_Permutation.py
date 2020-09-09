class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        self.res = []
        self.length = len(S)
        self.dfs(0, list(S))
        return self.res

    def dfs(self, index, s):
        if index == self.length:
            self.res.append(''.join(s))
            return
        if s[index].isdigit():
            self.dfs(index+1, s)
        else:
            s[index] = s[index].lower()
            self.dfs(index+1, s)
            s[index] = s[index].upper()
            self.dfs(index+1, s)