class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        steps = 0
        length = len(nums)
        double_times = 0
        for i in range(length):
            times = 0
            while nums[i] > 0:
                if nums[i] % 2:
                    steps += 1
                    nums[i] -= 1
                if nums[i]:
                    nums[i] //= 2
                    times += 1
            steps += times - double_times
            double_times =+ times
        return steps