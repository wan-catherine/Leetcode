class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        mapping = {}
        res = 0
        for i in arr:
            if i - difference in mapping:
                mapping[i] = mapping[i-difference] + 1
            else:
                mapping[i] = 1
            res = max(res, mapping[i])
            if res == 3:
                print(i)
        return res