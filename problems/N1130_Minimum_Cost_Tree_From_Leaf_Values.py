import sys


class Solution(object):
    def mctFromLeafValues_dp(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        length = len(arr)
        dp = [[sys.maxsize] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = 0
        for i in range(1, length):
            dp[i-1][i] = arr[i-1]*arr[i]

        for l in range(2, length+1):
            for i in range(length - l + 1):
                j = i + l - 1
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + max(arr[i:k+1])*max(arr[k+1:j+1]))
        return dp[0][-1]

    """
    The problem can translated as following:
    Given an array A, choose two neighbors in the array a and b,
    we can remove the smaller one min(a,b) and the cost is a * b.
    What is the minimum cost to remove the whole array until only one left?

    We calculate the prev_greater and next_greater, and use the min(prev_greater, next_greater) * a. 
    Use monotonic stack.
    """
    def mctFromLeafValues(self, arr):
        length = len(arr)
        stack = []
        next_greater = [sys.maxsize] * length
        for i in range(length):
            while stack and arr[stack[-1]] < arr[i]:
                next_greater[stack[-1]] = arr[i]
                stack.pop()
            stack.append(i)

        stack = []
        prev_greater = [sys.maxsize] * length
        for i in range(length):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            if stack:
                prev_greater[i] = arr[stack[-1]]
            stack.append(i)

        res = 0
        for i in range(length):
            if next_greater[i] == sys.maxsize and prev_greater[i] == sys.maxsize:
                continue
            res += arr[i] * min(next_greater[i], prev_greater[i])
        return res
