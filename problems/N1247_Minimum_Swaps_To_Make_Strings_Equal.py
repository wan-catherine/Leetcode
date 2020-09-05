import collections


class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        count = collections.Counter(s1+s2)
        for key in count:
            if count[key] % 2:
                return -1

        length = len(s1)
        x_num, y_num = 0, 0
        for i in range(length):
            if s1[i] == s2[i]:
                continue
            if s1[i] == 'x':
                x_num += 1
            else:
                y_num += 1
        x_div, x_mod = divmod(x_num, 2)
        y_div, y_mod = divmod(y_num, 2)
        res = x_div + y_div + (2 if x_mod != 0 else 0)
        return res


