"""
similar as problem 1296
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        num_count_mapping = {}
        for num in nums:
            if num in num_count_mapping:
                num_count_mapping[num] += 1
            else:
                num_count_mapping[num] = 1

        heads = []
        for num in num_count_mapping:
            if num-1 not in num_count_mapping:
                heads.extend([num] * num_count_mapping[num])

        res = 1
        while heads:
            head = heads.pop()
            if num_count_mapping[head] == 0:
                continue
            i = 1
            while head + i in num_count_mapping and num_count_mapping[head+i] > 0:
                num_count_mapping[head+i] -= 0
                i += 1
            res = max(res, i)
        return res
