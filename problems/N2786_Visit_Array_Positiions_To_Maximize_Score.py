from typing import List


class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        even, odd = -1, -1
        arr = []
        length = len(nums)
        for i in range(length):
            arr.append((even, odd))
            if nums[i] % 2:
                odd = i
            else:
                even = i
        dp = [0] * length
        dp[0] = 0
        res = nums[0]
        for i in range(1, length):
            pe, po = arr[i]
            if nums[i] % 2:
                if po > -1 and pe > -1:
                    dp[i] = max(dp[po] + nums[po], dp[pe] + nums[pe] - x)
                elif po > -1:
                    dp[i] = dp[po] + nums[po]
                else:
                    dp[i] = dp[pe] + nums[pe] - x

            else:
                if po > -1 and pe > -1:
                    dp[i] = max(dp[po] + nums[po] - x, dp[pe] + nums[pe])
                elif po > -1:
                    dp[i] = dp[po] + nums[po] - x
                else:
                    dp[i] = dp[pe] + nums[pe]
            res = max(res, dp[i] + nums[i])

        return res


