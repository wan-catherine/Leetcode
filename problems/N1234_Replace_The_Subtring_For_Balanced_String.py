import collections


class Solution(object):
    def balancedString_my(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        num = length // 4
        count = {'Q':0, 'W':0, 'E':0, 'R':0}
        for i in s:
            count[i] += 1

        updates = {}
        for key, value in count.items():
            if value > num:
                updates[key] = value - num
        if not updates:
            return 0

        start, end = 0, 0
        res = length
        while end < length:
            if s[end] in updates:
                updates[s[end]] -= 1
            while self.check(updates):
                if s[start] in updates:
                    updates[s[start]] += 1
                res = min(res, end - start + 1)
                start += 1
            end += 1

        if self.check(updates):
            res = min(res, end - start + 1)
        return res

    def check(self, updates):
        for key, value in updates.items():
            if value > 0:
                return False
        return True

    """
    Use collections.Counter and all function 
    """
    def balancedString(self, s):
        count = collections.Counter(s)
        res = n = len(s)
        i = 0
        for j, c in enumerate(s):
            count[c] -= 1
            while i < n and all(n / 4 >= count[c] for c in 'QWER'):
                res = min(res, j - i + 1)
                count[s[i]] += 1
                i += 1
        return res
