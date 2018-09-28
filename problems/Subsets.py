class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == None or len(nums) < 1:
            return [[]]

        nums = sorted(nums)
        res = [[] for i in range(len(nums))]
        for i in nums:
            res[0].append([i])

        for i in range(1, len(nums)):
            for l in res[i - 1]:
                if l[i - 1] == nums[-1]:
                    continue
                for j in nums[i:]:
                    if j <= l[i - 1]:
                        continue
                    lcopy = l.copy()
                    lcopy.append(j)
                    res[i].append(lcopy)
        result =[[]]
        for i in res:
            result.extend(i)
        return result



