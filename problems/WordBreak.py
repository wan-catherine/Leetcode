class Solution(object):
    def wordBreak_timeout(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if s == "":
            return True

        for word in wordDict:
            if not s.startswith(word):
                continue
            if self.helper(s[len(word):], wordDict, memo):
                return True
        memo[s] = False
        return False


    def wordBreak(self, s, wordDict):
        res = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i - len(w) + 1:i + 1] and (i - len(w) == -1 or res[i - len(w)]):
                    res[i] = True
        return res[-1]
