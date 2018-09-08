class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 1:
            return nums

        res = [[[nums[0]]]]
        for i in range(1,len(nums)):
            res.append([])
            num = nums[i]
            for l in res[i - 1]:
                for j in range(i + 1):
                    newL = l.copy()
                    newL.insert(j, num)
                    res[i].append(newL)
        return res[len(nums) -1]
