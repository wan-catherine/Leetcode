class Solution(object):
    def findTargetSumWays_dfs_tle(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.length = len(nums)
        nums_sum = sum(nums)
        if nums_sum < abs(S):
            return 0
        self.res = 0
        self.dfs(nums, S, 0)
        return self.res

    def dfs(self, nums, target, current):
        if current == self.length:
            if target == 0:
                self.res += 1
            return

        self.dfs(nums, target-nums[current], current+1)
        self.dfs(nums, target+nums[current], current+1)

    """
    DP:
    dp[i][j] : total ways to assign symbols to make sum of the first i integers equal to j .
    j can be range of [-sum(nums), sum(nums)] , but for index which can't be negative , so j is one of [0, 2*sum(nums)] --> [0: 2*sum(nums)+1]
    i is one of [1, len(nums)] --> [1:len(nums)+1]
    
    dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j+nums[i-1]]
    """
    def findTargetSumWays_slow(self, nums, S):
        length = len(nums)
        nums_sum = sum(nums)
        if nums_sum < abs(S):
            return 0

        sum_range = 2 * nums_sum + 1
        dp = [[0] * sum_range for _ in range(length + 1)]
        offset = nums_sum
        dp[0][offset] = 1

        for i in range(1, length + 1):
            for j in range(0, sum_range):
                if nums[i - 1] + j >= 0 and nums[i - 1] + j < sum_range:
                    dp[i][j] += dp[i - 1][nums[i - 1] + j]
                if j - nums[i - 1] >= 0 and j - nums[i - 1] < sum_range:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]

        return dp[length][S + offset]

    def findTargetSumWays(self, nums, S):
        length = len(nums)
        nums_sum = sum(nums)
        if nums_sum < abs(S):
            return 0

        sum_range = 2 * nums_sum + 1
        dp = [[0] * sum_range for _ in range(length + 1)]
        offset = nums_sum
        dp[0][offset] = 1

        # compare with last method , we don't need to check boundary conditions, save a lot of time.
        for i in range(1, length + 1):
            for j in range(nums[i-1], sum_range-nums[i-1]):
                if not dp[i-1][j]:
                    continue
                dp[i][j + nums[i-1]] += dp[i-1][j]
                dp[i][j - nums[i-1]] += dp[i-1][j]

        return dp[length][S+offset]

    """
    convert to subset (0-1 pack problem)
    P is the subset includes all positive numbers
    N is the subset includes all negative numbers
    P+N = S
    P-N = sum(nums)
    P+N+P-N = S + sum(nums) --> P = (S + sum(nums)) // 2 
    target = (S + sum(nums)) // 2 
    
    so we now need to find total ways of subsets of nums which equals to target.
    
    """
    def findTargetSumWays(self, nums, S):
        nums_sum = sum(nums)
        if (S + nums_sum) % 2 or nums_sum < abs(S):
            return 0
        target = (S + nums_sum) // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] += dp[j - num]

        return dp[-1]