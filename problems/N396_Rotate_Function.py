"""
f(i) = 0 * A[0] + 1 * A[1] + 2 * A[2] + .... + (k-1) * A[k-1] + k * A[k]
f(i+1) = 1 * A[0] + 2 * A[1] + 3 * A[2] + ... + k * A[k-1] + 0 * A[k]
=>f(i+1) - f(i) = A[0] + A[1] + A[2] + ... + A[k-1] - k * A[k]
                = (A[0] + A[1] + A[2] + ... + A[k-1] + A[k]) - (k+1) * A[k]
                = sum(Array) - A[k] * array.length
=> f(i+1) = f(i) + sum(Array) - last element * array.length

Here the A[k] will be the reverse of A.
"""
from typing import List


class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        r = curr = sum(i * j for i, j in enumerate(A))
        s = sum(A)
        k = len(A)
        while A:
            curr += s - A.pop() * k
            r = max(curr, r)
        return r

    def maxRotateFunction(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 0
        prefix, suffix = nums[:], [0] * length
        for i in range(1, length):
            prefix[i] += prefix[i - 1]
        for i in range(length - 2, -1, -1):
            suffix[i] += suffix[i + 1] + nums[i + 1]
        res = 0
        for i in range(length):
            res += i * nums[i]
        # print(res)
        # print(prefix)
        # print(suffix)
        pre = res
        for i in range(1, length):
            pre -= (length - 1) * nums[-i]
            pre += prefix[length - i - 1]
            pre += suffix[length - i]
            res = max(res, pre)
            # print(pre)
        return res