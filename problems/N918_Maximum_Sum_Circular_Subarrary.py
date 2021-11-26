"""
first need to know Kadane Algorithm which actually is a dp method.
    d[i] means current max value for the subarray, it has two situations:
        1. d[i] = d[i-1]+A[i]
        2. d[i] = A[i]
    d[i] = max(#1, #2) for max value
    d[i] = min(#1, #2) for min value
    here is a good explaination :
    https://www.youtube.com/watch?v=2MmGzdiKR9Y

    here is diagram to understand the DP:
    * * * * * * * *
           2-
          -1-
        - -1-
      - - -1-
    - - - -1-
so here is we want to know max value for the subarray of the 5th : A[:5] , the brutal solution is
    max(A[4], A[3]+A[4], A[2]+A[3]+A[4], A[1]+A[2]+A[3]+A[4], A[0]+A[1]+A[2]+A[3]+A[4])
Let's see the max value for the subarray of the 4th : a[:4] , the brutal solution is :
    max(A[3], A[2]+A[3], A[1]+A[2]+A[3], A[0]+A[1]+A[2]+A[3])

Then we can see it : d[i]=max(A[i] , d[i-1]+A[i])

second about the circular subarray :
    there are two situations:
        1. maximum subarray is in the array which is the normal Kadane Algorithm
        2. maximum subarray is in teh circular one :
            we can find the minimum subarray of the array,
            then sum(A) - minimum subarray value = maximum
    There is a special case : which all numbers in array are negative :
        sum(A) == minimum subarray value
    at this time, return maximum subarray value which should be the minimum single value in the array
"""
from typing import List


class Solution:
    def maxSubarraySumCircular(self, A) -> int:
        if len(A) == 1:
            return A[0]
        min_subarry_sum = self.getMaxSum([-i for i in A])
        temp = sum(A)+min_subarry_sum
        max_subarray_sum = self.getMaxSum(A)
        return  max(temp, max_subarray_sum ) if temp != 0 else max_subarray_sum

    def getMaxSum(self, A):
        current_value = A[0]
        max_value = A[0]
        for n in A[1:]:
            current_value = max(n, n+current_value)
            max_value = max(current_value, max_value)
        return max_value

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        has_positive = False
        for n in nums:
            if n > 0:
                has_positive = True
                break
        if not has_positive:
            return max(nums)

        total = sum(nums)
        length = len(nums)
        dpmax = [0] * length
        dpmin = [0] * length
        dpmax[0] = dpmin[0] = nums[0]
        res = nums[0]
        for i in range(1, length):
            dpmax[i] = max(dpmax[i - 1], 0) + nums[i]
            dpmin[i] = min(dpmin[i - 1], 0) + nums[i]
            res = max(res, dpmax[i], total - dpmin[i])
        return res