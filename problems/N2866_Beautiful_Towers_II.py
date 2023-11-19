from typing import List


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        maxHeights = [0] + maxHeights + [0]
        length = len(maxHeights)
        def helper(arr):
            stack = [0]
            ans = [0] * length
            for i in range(1, length - 1):
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()
                idx = stack[-1]
                stack.append(i)
                ans[i] = ans[idx] + (i - idx) * arr[i]
            return ans

        left = helper(maxHeights)
        right = helper(maxHeights[::-1])[::-1]
        res = 0
        for i in range(length):
            res = max(res, left[i] + right[i] - maxHeights[i])
        return res


