class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        nums_sum = sum(nums)
        target = nums_sum % p
        if not target:
            return 0
        prefix = nums[:]
        length = len(nums)
        count = length
        for i in range(1, length):
            prefix[i] += prefix[i-1]

        mapping = {0:0}
        for i, n in enumerate(nums):
            val = (prefix[i] % p - target) % p
            if val in mapping and mapping[val] <= i:
                count = min(count, i - mapping[val] + 1)
            mapping[prefix[i] % p] = i + 1
        # print(mapping)
        return count if count != length else -1

