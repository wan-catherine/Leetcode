"""
Min-Max Strategy:
Always pick the best and your opponent will do the same thing.
"""
from typing import List


class Solution(object):
    """
    dp[i][j] : for nums[i:j+1] , the maximum scores play1 can get .
    dp[i][j][0] = max(dp[i+1][j][1] + nums[i], dp[i][j-1][1] + nums[j])
    Notice , here we use the second value.Because when play1 chooses i, or j-1 then the left dp[i+1][j] or dp[i][j-1] will be start
    from play2. So we need to use the second value .
    """
    def PredictTheWinner_dp(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length <= 2:
            return True
        dp = [[(0,0)]*length for _ in range(length)]
        for i in range(length):
            dp[i][i] = (nums[i], 0)

        for l in range(2, length+1):
            for i in range(length):
                j = i + l - 1
                if j >= length:
                    continue
                if dp[i+1][j][1] + nums[i] > dp[i][j-1][1] + nums[j]:
                    dp[i][j] = (dp[i+1][j][1] + nums[i], dp[i+1][j][0])
                else:
                    dp[i][j] = (dp[i][j-1][1] + nums[j], dp[i][j-1][0])
        # print(dp)
        return dp[0][-1][0] >= dp[0][-1][1]

    def PredictTheWinner_(self, nums):
        self.memo = {}
        # return self.get_score(nums, 0, len(nums)-1) >= 0
        res = self.get_score(nums, 0, len(nums)-1)
        return res[0] >= res[1]

    def get_score(self, nums, l, r):
        if l == r:
            return nums[l]
        if (l,r) in self.memo:
            return self.memo[(l, r)]
        res = max(nums[l] - self.get_score(nums, l+1, r), nums[r] - self.get_score(nums, l, r-1))
        self.memo[(l,r)] = res
        return res

    def get_score(self, nums, l, r):
        if l == r:
            return nums[l],0
        if (l,r) in self.memo:
            return self.memo[(l, r)]
        left =  self.get_score(nums, l+1, r)
        right = self.get_score(nums, l, r-1)
        if nums[l] + left[1] >= nums[r] + right[1]:
            res = (nums[l] + left[1], left[0])
        else:
            res = (nums[r] + right[1], right[0])
        self.memo[(l,r)] = res
        return res

    """
    dp[i][j] : the maximum scores first player can get from nums[i~j] 
    """
    def PredictTheWinner(self, nums: List[int]) -> bool:
        length = len(nums)
        prefix = [0] + nums[:]
        for i in range(length):
            prefix[i+1] += prefix[i]

        dp = [[0] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = nums[i]

        for l in range(2, length+1):
            for i in range(length-l+1):
                j = i + l - 1
                dp[i][j] = max(nums[i] + prefix[j+1] - prefix[i+1] - dp[i+1][j], nums[j] + prefix[j] - prefix[i] - dp[i][j-1])
        return dp[0][-1] >= prefix[-1] / 2