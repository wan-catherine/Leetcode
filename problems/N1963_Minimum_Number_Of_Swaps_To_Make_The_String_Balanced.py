class Solution:
    def minSwaps(self, s: str) -> int:
        cur, res = 0, 0
        for c in s:
            if c == '[':
                cur += 1
            else:
                cur -= 1
                if cur < 0:
                    res += 1
                    cur += 2
        return res
