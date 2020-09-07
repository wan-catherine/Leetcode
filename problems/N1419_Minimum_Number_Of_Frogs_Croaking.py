import collections


class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        # length = len(croakOfFrogs)
        # if length % 5:
        #     return -1
        # counter = collections.Counter(croakOfFrogs)
        # for c in 'croak':
        #     if c not in counter:
        #         return -1
        #     if counter[c] != length//5:
        #         return -1

        status = collections.defaultdict(int)
        res = 0
        temp = 0
        for c in croakOfFrogs:
            if c == 'r':
                if status['c'] < 1:
                    return -1
                status['c'] -= 1
                temp -= 1
            elif c == 'o':
                if status['r'] < 1:
                    return -1
                status['r'] -= 1
                temp -= 1
            elif c == 'a':
                if status['o'] < 1:
                    return -1
                status['o'] -= 1
                temp -= 1
            elif c == 'k':
                if status['a'] < 1:
                    return -1
                status['a'] -= 1
                temp -= 1
            if c != 'k':
                status[c] += 1
                temp += 1
            res = max(res, temp)
        if temp != 0:
            return -1
        return res

