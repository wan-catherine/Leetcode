"""
https://www.youtube.com/watch?v=uAGt1QoAoMU

first need to change all zero to -1, so for equal numbers of 0 and 1, the sum will be zero

use prefix sum to check
create a dictionary which key is the sum of the first i nums
and value is the first index for such sum

so if the same same shows again which means during this index from the last time,
all numbers between them are sum = 0

for example:
nums = [0,1,0]  --> [-1,1,-1]
dictionary : {-1:0, 0:1}, then for nums[2], the sum == -1 so here 2-0 = 2

"""

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        sum_dict = {}
        nums_len = len(nums)
        sum = 0
        res = 0
        for i in range(nums_len):
            sum += 1 if nums[i] == 1 else -1
            if sum not in sum_dict:
                sum_dict[sum] = i
            else:
                res = max(res, i - sum_dict[sum])
            if sum == 0:
                res = max(res, i + 1)
        return res



