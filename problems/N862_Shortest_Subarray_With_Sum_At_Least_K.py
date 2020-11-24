import sys
from collections import deque
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
            while arr and prefix[arr[0]] <=prefix[i] - K:
                index = arr.popleft()
            res = min(res, i - index)
            while arr and prefix[arr[-1]] >= prefix[i]:
                arr.pop()
            arr.append(i)

        return -1 if res == sys.maxsize else res


