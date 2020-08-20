class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        length = len(s)
        if length < k:
            return False
        nums = set()
        start, end = 0, k-1
        while end < length:
            val = int(s[start:end+1], 2)
            nums.add(val)
            start += 1
            end += 1
        if len(nums) == 2**k:
            return True
        return False