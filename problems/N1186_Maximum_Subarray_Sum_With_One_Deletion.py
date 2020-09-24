"""
dp[i] : the maximum sum for the subset which ends with ith element in the arr .
for kadane's Algo:
dp[i] = max(dp[i-1] + arr[i], arr[i])
if dp[i-1] < 0, it will be just arr[i].

For this problem, it can at most delete one element. So we have one more status:
dp[i][0] : the maximum sum for the subset which ends with ith element in the arr without deletion.
dp[i][1] : the maximum sum for the subset which ends with ith element in the arr with one deletion.
"""
class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        length = len(arr)
        if length == 1:
            return arr[0]

        dp = [[0]*2 for _ in range(length)]
        dp[0][0] = arr[0]
        dp[0][1] = 0
        res = arr[0]
        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0] + arr[i], arr[i])
            dp[i][1] = max(dp[i-1][0], dp[i-1][1] + arr[i])
            res = max(res, dp[i][0], dp[i][1])
        return res
