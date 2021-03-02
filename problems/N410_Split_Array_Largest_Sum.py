import sys


class Solution(object):
    """
    Binary search:
    use the subarry's sum as the mid value.

    """
    def splitArray_bs(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def check(val, m):
            count = 1
            v = 0
            for n in nums:
                if n > val:
                    return False
                if v+n <= val:
                    v += n
                else:
                    count += 1
                    v = n
            return count <= m

        left, right = 0, 10**9 + 1
        while left <= right:
            mid = (right - left) // 2 + left
            if check(mid, m):
                right = mid - 1
            else:
                left = mid + 1
        return left

    """
    dp[i][j]: nums[0:i] divide j groups. 
    dp[i][j] = min( max(dp[k][j-1], sum(nums[j:k]) for k in [j,i]))
    """
    def splitArray_TLE(self, nums, m):
        nums = [0] + nums
        length = len(nums)
        dp = [[sys.maxsize]*(m+1) for _ in range(length)]
        dp[0][0] = 0

        for i in range(1, length):
            v = min(i, m) + 1
            for j in range(1, v):
                s = 0
                for k in range(i, j-1, -1):
                    s += nums[k]
                    dp[i][j] = min(dp[i][j], max(dp[k-1][j-1], s))
        return dp[-1][-1]
