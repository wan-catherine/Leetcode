class Solution(object):
    def singleNumber_sum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (3*sum(set(nums)) - sum(nums)) / 2

    def singleNumber(self, nums):
        number, res = 0, 0
        for i in range(64):
            number = 0
            for k in nums:
                number += (k >> i) & 1
            res |= (number) % 3 << i
        return res