from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def strStr(haystack, needle):
            if not needle:
                return 0
            lh, ln = len(haystack), len(needle)
            pattern = [0] * ln
            for i in range(1, ln):
                l = pattern[i - 1]
                while l > 0 and needle[l] != needle[i]:
                    l = pattern[l - 1]
                if needle[l] == needle[i]:
                    l += 1
                pattern[i] = l

            res = []
            l = 0
            for i in range(lh):
                while l > 0 and haystack[i] != needle[l]:
                    l = pattern[l - 1]
                if haystack[i] == needle[l]:
                    l += 1
                if l == ln:
                    res.append(i - l + 1)
                    l = pattern[l - 1]
            return res

        aa = strStr(s, a)
        bb = strStr(s, b)
        laa, lbb = len(aa), len(bb)
        i, j = 0, 0 
        res = []
        while i < laa and j < lbb:
            v = abs(aa[i] - bb[j])
            if v <= k:
                res.append(aa[i])
                i += 1 
            else:
                if bb[j] > aa[i]:
                    i += 1
                else:
                    j += 1 
        return res 