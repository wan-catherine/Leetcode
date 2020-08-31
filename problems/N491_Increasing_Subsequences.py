class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        self.length = len(nums)
        if self.length < 2:
            return []
        res = []
        self.dfs(0, nums, res, [])
        print(res)
        return res

    def dfs(self, index, nums, res, temp):
        if len(temp) > 1:
            res.append(temp[:])
        if index == self.length:
            return
        visited = set()
        for i in range(index, self.length):
            if len(temp) >= 1 and nums[i] < temp[-1]:
                continue
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            temp.append(nums[i])
            self.dfs(i+1, nums, res, temp)
            temp.pop()



