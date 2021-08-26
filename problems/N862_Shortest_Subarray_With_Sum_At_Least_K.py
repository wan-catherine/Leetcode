import collections
import sys
from collections import deque
from typing import List

"""
Basical idea: use the prefix sum array. For j-th , find an i-th (i < j ) which prefix[j] - prefix[i] >= k 
it's a O(N*N), so we need to do prune. 

Use greedy idea :
use a deque to maintain all before prefix index. 
Let's say we have a, b, c, d, e, f, g in the deque. Then we now have j ==> prefix[j] == x. 
We need to insert x into deque. 

we can search from the left-most, and if (a, b, c) + k <= x , then c will be the nearest number to x. 
At the same time we can remove all a, b, c . Because for the future, j+1/2/3..., even though prefix[j+i] - c >= k, it won't be 
better than j . 
Then we can update the res.
Then need to insert j into the deque. 
For the right side, we can pop out all e,f,g which >= prefix[j], because prefix[j] is smaller and j is largert index than them. 

The key point is : 
    We need to find a index which is as large as possible and prefix[index] as small as possible. 
"""

class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A = [0] + A
        length = len(A)
        prefix = [0] * length
        for i in range(1, length):
            prefix[i] = prefix[i-1] + A[i]

        arr = deque([0])
        res = sys.maxsize
        for i in range(1, length):
            index = -sys.maxsize
            while arr and prefix[arr[0]] <= prefix[i] - K:
                index = arr.popleft()
            res = min(res, i - index)
            while arr and prefix[arr[-1]] >= prefix[i]:
                arr.pop()
            arr.append(i)
        return -1 if res == sys.maxsize else res

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        length = len(nums)
        if k <= nums[0]:
            return 1
        arr = collections.deque([(nums[0], 0)])
        res = sys.maxsize
        prefix = nums[0]
        for i in range(1, length):
            prefix += nums[i]
            if prefix >= k:
                res = min(res, i+1)
            index = -sys.maxsize
            while arr:
                if arr[0][0] + k <= prefix:
                    index = max(index, arr[0][1])
                    arr.popleft()
                else:
                    break
            if index >= 0:
                res = min(res, i - index)
            while arr:
                p, idx = arr[-1]
                if p >= prefix:
                    arr.pop()
                else:
                    break
            arr.append((prefix, i))
        return res if res < sys.maxsize else -1


