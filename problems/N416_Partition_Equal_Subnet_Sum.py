class Solution:
    def canPartition_timeout(self, nums):
        sum_nums = sum(nums)
        if sum_nums % 2:
            return False
        dp = [0]
        flag = sum_nums / 2
        for num in nums:
            temp = dp[:]
            for i in temp:
                value = num + i
                if value == flag:
                    return True
                dp.append(value)
        return False

    def canPartition_two_array(self, nums):
        sum_nums = sum(nums)
        if sum_nums % 2:
            return False
        dp = [1] + [0] * sum_nums
        for num in nums:
            temp = dp[:]
            for i in range(len(dp)):
                if temp[i]:
                    dp[i+num] = 1
            if dp[sum_nums//2]:
                return True
        return False

    def canPartition(self, nums):
        sum_nums = sum(nums)
        if sum_nums % 2:
            return False
        dp = [1] + [0] * sum_nums
        for num in nums:
            for i in range(sum_nums, -1, -1):
                if dp[i]:
                    dp[i+num] = 1
            if dp[sum_nums//2]:
                return True
        return False