class Solution:
    def maxCoins_(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0
        l = len(nums)

        res = [[0]* l for i in nums]

        n = 1
        while n <= l:
            for i in range(l):
                if i + n > l:
                    continue
                maxN = 0
                for j in range(n):
                    temp = nums[i+j]
                    if i > 0:
                        temp *= nums[i-1]
                    if l - i - n > 0:
                        temp *= nums[i+n]
                    if j == 0 and i + 1 < l:
                        temp += res[i+1][i+n-1]
                    if j + 1 == n:
                        temp += res[i][i+n-2]
                    if j > 0 and j < n - 1:
                        temp += res[i][i+j-1] + res[i+j+1][i+n-1]
                    maxN = max(temp, maxN)

                res[i][i+n-1] = maxN
            n += 1
        return res[0][-1]

    """
    Classical DP interval problem!!!
    dp[i][j]: between i ~ j (inclusive), the maximum coins you can collect by bursting the balloons  between [i,j]
    
    then for k which [i,j] (inclusive) ==>
    dp[i][j] = dp[i][k-1] + (burst the last k) + dp[k+1][j]
        1. burst all balloons at left of k , get dp[i][k-1] coins
        2. burst all balloons at right of k , get dp[k+1][j] coins 
        3. the burst k , here the left of k is nums[i-1] and, the right of k is nums[j+1]
        
        Because k the last balloon bursted in between [i, j], so it can make sure nums[i-1] and nums[j+1] always existed!!!
    """
    def maxCoins(self, nums):
        if not nums:
            return 0
        length = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (length + 2) for _ in range(length + 2)]

        for l in range(1, length + 1):
            for left in range(1, length + 2 - l):
                right = left + l - 1
                for k in range(left, right + 1):
                    dp[left][right] = max(dp[left][right], dp[left][k-1] + dp[k+1][right] + nums[left-1] * nums[k] * nums[right+1])
        return dp[1][length]


