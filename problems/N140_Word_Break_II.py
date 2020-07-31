class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.wordDict = set(wordDict)
        return self.search(s, {})

    def search(self, s, memo):
        if s in memo:
            return memo[s]

        ans = []
        if s == "":
            ans.append(s)
            return ans

        for word in self.wordDict:
            if s.startswith(word):
                substrings = self.search(s[len(word):], memo)
                for sub in substrings:
                    opt = " " if sub else ''
                    ans.append(word + opt + sub)
        # print(ans)
        memo[s] = ans
        return ans

