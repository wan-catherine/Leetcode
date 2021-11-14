"""
First , I think about the intervals , then everything becomes too complicated.

Then, reading other's answer, there is a way to increase all needed number to the number+1 .

Keypoint:
 move to next : a[i] -> a[i+1]
"""
import sys
from typing import List


class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        A.sort()
        length = len(A)
        res = 0
        for i in range(1, length):
            if A[i] <= A[i-1]:
                res += A[i-1] - A[i] + 1
                A[i] = A[i-1] + 1
        return res

    def minIncrementForUnique(self, nums: List[int]) -> int:
        arr = [0] * (10 ** 5 + 1)
        minimum = sys.maxsize
        maxsize = 0
        for n in nums:
            arr[n] += 1
            minimum = min(minimum, n)
            maxsize = max(maxsize, n)
        res = 0
        flag = False
        for n in range(minimum, maxsize + 1):
            if n >= 10 ** 5:
                flag = True
                break
            if arr[n] > 1:
                res += arr[n] - 1
                arr[n + 1] += arr[n] - 1
        if flag:
            res += (1 + arr[-1] - 1) * (arr[-1] - 1) // 2
        if arr[maxsize+1] > 1:
            res += (1 + arr[maxsize+1] - 1) * (arr[maxsize+1] - 1) // 2
        return res
