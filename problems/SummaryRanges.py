class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums == None or len(nums) < 1:
            return []
        res = [str(nums[0])]
        base = nums[0]

        for i in range(1,len(nums)):
            if nums[i] != base + 1 :
                if res[-1] != str(base):
                    res[-1] += "->" + str(base)
                res.append(str(nums[i]))
            base = nums[i]
            if i == len(nums) - 1 and res[-1] != str(base):
                res[-1] += "->" + str(base)
        return res

