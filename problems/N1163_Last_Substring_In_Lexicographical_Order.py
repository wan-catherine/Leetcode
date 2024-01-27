"""
need to remove which has same prefix substring
b***b***@@@@@ > b***@@@@@

where offset , it means b[i:i+offset] for all candidates substring should be equal .
"""
class Solution:
    def lastSubstring(self, s: str) -> str:
        length = len(s)
        cmax = max(s)
        candidates = [i for i in range(length) if s[i] == cmax]
        offset = 1
        while len(candidates) > 1:
            curmax = max(s[i+offset] for i in candidates if i + offset < length)
            cnxt = []
            for i, c in enumerate(candidates):
                # remove which has the same prefix substring
                if i > 0 and candidates[i-1] + offset == c:
                    continue
                if c + offset < length and s[c + offset] == curmax:
                    cnxt.append(c)
            candidates = cnxt
            offset += 1
        return s[candidates[0]:]