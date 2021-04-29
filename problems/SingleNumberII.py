class Solution(object):
    def singleNumber_sum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (3*sum(set(nums)) - sum(nums)) / 2

    """
    python negative number need to ~(res ^ 0xffffffff)
    """
    def singleNumber(self, nums):
        number, res = 0, 0
        for i in range(32):
            number = 0
            for k in nums:
                number += (k >> i) & 1
            res |= (number) % 3 << i
        return res if (number % 3) == 0 else ~(res ^ 0xffffffff)