"""
Backtracing

Notice, when adding path into results, need to add the copy of the path , not directly path itself.
 res.append(path[:])
"""
class Solution:
    def permute_before(self, nums):
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

    def permute(self, nums):
        res = []
        self.backtracing([], nums, res)
        return res

    def backtracing_for_distinct(self, path, nums, res):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if nums[i] in path:
                continue
            path.append(nums[i])
            self.backtracing(path, nums, res)
            path.pop()

    def backtracing(self, path, nums, res):
        if not nums:
            res.append(path[:])
            return
        for i in range(len(nums)):
            path.append(nums[i])
            self.backtracing(path, nums[:i] + nums[i+1:], res)
            path.pop()



