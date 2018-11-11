class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == None or len(s) <= 1:
            return s

        i = 1
        res = ""
        temp = ""
        while i < len(s):
            if i+1 < len(s) and s[i-1] == s[i+1]:
                temp = s[i-1:i+2]
                p = i - 2
                q = i + 2
                if s[i-1] == s[i]:
                    while p >= 0:
                        if s[p] == s[i-1]:
                            p -= 1
                        else:
                            break
                    while q < len(s):
                        if s[q] == s[i]:
                            q += 1
                        else:
                            break
                    temp= s[p+1:q]

                while p >=0 and q <len(s):
                    if s[p] == s[q]:
                        temp = s[p:q+1]
                        p -= 1
                        q += 1
                    else:
                        break
            elif s[i-1] == s[i]:
                temp = s[i-1:i+1]
                p = i-2
                q = i+1
                while p >= 0 and q < len(s):
                    if s[p] == s[q]:
                        temp = s[p:q + 1]
                        p -= 1
                        q += 1
                    else:
                        break
            res = temp if len(temp) > len(res) else res
            i += 1
        if len(res) == 0:
            return s[0]
        return res






