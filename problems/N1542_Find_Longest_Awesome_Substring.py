"""
Smiliar as 1371
The only diffierent is we have any number as middle character or don't have a middle character
"""
class Solution(object):
    def longestAwesome(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        index_mapping = {0:-1}
        key = 0
        res = 0
        for i in range(length):
            key ^= (1 << int(s[i]))
            if key not in index_mapping:
                index_mapping[key] = i
            for j in range(10):  # this part is check we have any number as a middle character
                new_key = key ^ (1 << j)
                if new_key in index_mapping:
                    res = max(res, i - index_mapping[new_key])
            res = max(res, i - index_mapping[key])
        return res
