"""
Because those duplicated number only can show twice ,not 3,4....
So we can flip it , when second time meet the number , it will flip again.

So next time, meet problems say twice ,we can use this method.
"""
class Solution(object):
    def findDuplicates_still_use_extra_space(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = [0] * (len(nums) + 1)
        res = []
        for num in nums:
            if temp[num] != 0:
                res.append(num)
            else:
                temp[num] = num
        return res

    def findDuplicates(self, nums):
        res = []
        for i in nums:
            if nums[abs(i)-1] < 0:
                res.append(abs(i))
            else:
                nums[abs(i)-1] = - nums[abs(i)-1]
        return res