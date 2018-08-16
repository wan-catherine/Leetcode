class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1:
            return ""

        base = strs[0]
        res = ""
        for i in range(len(base)):
            flag = True
            for word in strs[1:]:
                if (i < len(word) and base[i] != word[i]) or i >= len(word):
                    flag = False
                    break
            if flag:
                res += base[i]
            else:
                break
        return res
