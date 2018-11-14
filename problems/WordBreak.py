class Solution(object):
    def wordBreak_timeout(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dictstr = ''.join(wordDict)
        for i in set(s):
            if i not in dictstr:
                return False
        return self.helper(s, wordDict)

    def helper(self, s, wordDict):
        if s == "":
            return True
        while s != "":
            l = [word for word in wordDict if s[0:len(word)] == word]
            if l == None or len(l) == 0:
                return False
            # l.sort(key=len)
            # l=l[::-1]
            for w in l:
                if self.helper(s[len(w):], wordDict) == True:
                    return True
            return False

    def wordBreak(self, s, wordDict):
        res = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i - len(w) + 1:i + 1] and (i - len(w) == -1 or res[i - len(w)]):
                    res[i] = True
        return res[-1]
