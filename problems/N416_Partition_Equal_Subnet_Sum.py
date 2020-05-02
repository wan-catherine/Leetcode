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

    def canPartition_before(self, nums):
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

# d[i][j] : by using the first i nums, the totally sum is j, then it's doable or not
# d[i][j] seperate two situations :
#         1. not used the ith num : d[i-1][j]
#         2. used the ith num : d[i-1][j - nums[i-1]]
# d[i][j] = d[i-1[j] or d[i-1][j - nums[i-1]]
# Here because we can reuse the number in nums, so for the second situation, it's d[i-1] not
# d[i] (for 322, 518, it will be d[i], because the coins there is infinite)
# also need to check if j - nums[i-1] >= 0


    def canPartition(self, nums):
        sum_nums = sum(nums)
        if sum_nums % 2:
            return False
        dp = [True] +[False] * sum_nums
        for i in range(1,len(nums)+1):
            before_dp = dp[:]
            for j in range(1, sum_nums+1):
                if j - nums[i-1] >= 0:
                    dp[j] = dp[j] or before_dp[j-nums[i-1]]
            if dp[sum_nums//2]:
                return True
        return False
