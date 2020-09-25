import collections


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        res = []
        nums = [str(i) for i in nums]
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if nums[i]+nums[j] < nums[j]+nums[i]:
                    nums[i],nums[j] = nums[j],nums[i]
            res.append(nums[i])
        if res and res[0][0] == '0':
            return '0'
        return ''.join(res)

    def largestNumber_others(self, nums):
        class LargerNumKey(str):
            def __lt__(x, y):
                return x + y > y + x

        nums = [str(i) for i in nums]
        res = sorted(nums, key=LargerNumKey)
        if res[0] == '0':
            return '0'
        return ''.join(res)