import collections


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums_set = set(nums)
        counter = collections.Counter(nums)
        res = 0
        for num in nums_set:
            if k == 0 and counter[num] > 1:
                counter[num] = 0
                res += 1
            elif k != 0:
                if num - k in nums_set and counter[num - k] > 0:
                    res += 1
                if num + k in nums_set and counter[num + k] > 0:
                    res += 1
                counter[num] = 0
        return res