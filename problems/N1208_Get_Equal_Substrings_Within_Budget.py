class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        length = len(s)
        diffs = []
        for i in range(length):
            diffs.append(abs(ord(s[i]) - ord(t[i])))

        left, right = 0, 0
        temp = 0
        res = 0
        while right < length:
            temp += diffs[right]
            while temp > maxCost:
                temp -= diffs[left]
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res