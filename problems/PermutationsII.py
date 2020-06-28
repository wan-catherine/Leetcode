class Solution:
    def permuteUnique_myselfversion(self, nums):
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
                    before = j - 1
                    if before >= 0 and nums[before] == num:
                        continue
                    newL = l.copy()
                    newL.insert(j, num)
                    if newL in res[i]:
                        continue
                    res[i].append(newL)
        return res[len(nums) -1]

    def permuteUnique_before(selfs, nums):
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l) + 1):
                    new_ans.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i] == n: #this is the key point
                        break

            ans = new_ans

        return ans

    def permuteUnique(self, nums):
        self.length = len(nums)
        nums.sort()
        res = []
        self.backtracking([], nums, res)
        return res

    def backtracking(self, path,  nums, res):
        if len(path) == self.length:
            res.append(path[:])
            return
        for i in range(len(nums)):
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                continue
            path.append(nums[i])
            self.backtracking(path, nums[:i]+nums[i+1:], res)
            path.pop()
