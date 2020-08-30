class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.length = len(nums)
        if self.length < 4:
            return False
        nums_sum = sum(nums)
        if nums_sum % 4 :
            return False
        nums.sort(reverse=True)
        if nums[0] > nums_sum//4:
            return False
        siders = [0]*4

        return self.dfs(0, siders, nums, nums_sum//4)

    def dfs(self, index, siders, nums, value):
        if index >= self.length:
            for i in siders:
                if i != value:
                    return False
            return True

        for i in range(4):
            if siders[i] + nums[index] > value:
                continue
            siders[i] += nums[index]
            if self.dfs(index + 1, siders, nums, value):
                return True
            siders[i] -= nums[index]
        return False

