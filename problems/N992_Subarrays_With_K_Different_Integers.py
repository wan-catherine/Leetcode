import collections
from bisect import bisect
from typing import List

"""
exactly(K) = atMost(K) - atMost(K-1)

Understanding about : res += end - start + 1
for [1,2], it will have end - start + 1 == 1 - 0 + 1 == 2 subarrays which the number of different integers is <= K
add one more : [1,2,1], then it has three subarrays which all end by [1]:
    [1,2,1], [2,1], [1]

add one more : [1,2,1,2], then it has 4 subarrays which all end by [2]:
    [1,2,1,2], [2,1,2], [1,2], [2]
    
So for all arrays, the number of subarrays equals to it's length!!!

"""

class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        self.length = len(A)
        self.arr = A
        return self.atMost(K) - self.atMost(K - 1)

    """
    I first directly use len(dict) and it very slow. 
    Here use l to track the len(dict) much faster.
    """
    def atMost(self, k):
        start, end, l = 0, 0, 0
        res = 0
        count = collections.defaultdict(int)
        while end < self.length:
            if not count[self.arr[end]] :
                count[self.arr[end]] = 1
                l += 1
                while l > k:
                    count[self.arr[start]] -= 1
                    if count[self.arr[start]] == 0:
                        l -= 1
                    start += 1
            else:
                count[self.arr[end]] += 1
            res += end - start + 1  #key part
            end += 1
        return res

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        length = len(nums)
        status = set()
        indexes = [-1] * (length + 1)
        l, r = 0, 0
        res = 0
        arr = []
        while r < length:
            if indexes[nums[r]] < 0:
                status.add(nums[r])
            else:
                idx = bisect.bisect_left(arr, indexes[nums[r]])
                arr.remove(arr[idx])
            bisect.insort_left(arr, r)
            indexes[nums[r]] = r
            if len(status) > k:
                l = arr[0] + 1
                status.remove(nums[arr[0]])
                indexes[nums[arr[0]]] = -1
                arr = arr[1:]
            if len(status) == k:
                res += arr[0] - l + 1
            r += 1
        return res

    def subarraysWithKDistinct_20250317(self, nums: List[int], k: int) -> int:
        length = len(nums)
        def atMost(m):
            if m == 0:
                return 0
            j, res = 0, 0
            status = collections.defaultdict(int)
            for i in range(length):
                while j < length and (nums[j] in status or len(status) < m):
                    status[nums[j]] += 1
                    j += 1
                res += j - i
                if status[nums[i]] == 1:
                    del status[nums[i]]
                else:
                    status[nums[i]] -= 1
            return res
        return atMost(k) - atMost(k-1)