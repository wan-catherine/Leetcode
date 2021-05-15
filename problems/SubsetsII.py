from typing import List


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

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []

        def dfs(index, cur):
            res.append(cur)
            pre = None
            for i in range(index, length):
                if pre is not None and nums[i] == nums[pre]:
                    continue
                else:
                    pre = i
                cur.append(nums[i])
                dfs(i + 1, cur[:])
                cur.pop()

        dfs(0, [])
        print(res)
        return res

