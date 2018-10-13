class Solution:
    # backtracking
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if nums == None or len(nums) < 1:
            return res.append([])

        nums = sorted(nums)
        subset = []
        self.toFindAllSubsets(nums, res, subset, 0)
        return res

    def toFindAllSubsets(self, nums, res, subset, index):
        res.append(subset.copy())

        for i in range(index, len(nums)):
            if i != index and nums[i - 1] == nums[i]:
                continue

            subset.append(nums[i])
            self.toFindAllSubsets(nums, res, subset, i+1)
            subset.pop()


