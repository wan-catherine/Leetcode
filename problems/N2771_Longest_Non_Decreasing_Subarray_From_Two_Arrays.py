from typing import List


class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        length = len(nums1)
        dp = [[0,0] for _ in range(length)]
        dp[0][0], dp[0][1] = 1, 1
        res = 1
        for i in range(1, length):
            p, q = max(nums1[i], nums2[i]), min(nums1[i], nums2[i])
            fp, fq = max(nums1[i-1], nums2[i-1]), min(nums1[i-1], nums2[i-1])
            if q >= fp:
                dp[i][1] = max(dp[i-1]) + 1
            elif q >= fq:
                dp[i][1] = dp[i-1][1] + 1
            else:
                dp[i][1] = 1
            if p >= fp:
                dp[i][0] = max(dp[i-1]) + 1
            elif p >= fq:
                dp[i][0] = dp[i-1][1] + 1
            else:
                dp[i][0] = 1
            res = max(res, dp[i][0], dp[i][1])
        return res