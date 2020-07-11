class Solution:
    def subsets_before(self, nums):
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

    # 20200711
    """
    Backtracking
    The key point is : use [] --> nums , if we use nums --> [], it will has a lot of duplicated array.
    """
    def subsets(self, nums):
        res = []
        if not nums:
            return res

        self.length = len(nums)
        self.backtrack(res, nums, [], 0)
        return res

    def backtrack(self, res, nums, temp, start):
        res.append(temp[:])
        for i in range(start, self.length):
            temp.append(nums[i])
            self.backtrack(res, nums, temp, i + 1)
            temp.pop()





