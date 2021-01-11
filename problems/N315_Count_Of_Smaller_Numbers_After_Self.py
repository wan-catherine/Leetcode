import bisect
"""
from right to left , to find the right position to insert the number . 
We can use binary search to find this position . 
Here I use python module to do so . 

We can write binary search by ourself, but need to deal with duplicated number.
"""

class Solution(object):
    def countSmaller_(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums

        nums_len = len(nums)
        res = [0] * nums_len
        temp = [nums[-1]]
        for i in range(nums_len-2, -1, -1):
            index = bisect.bisect_left(temp,nums[i])
            bisect.insort_left(temp, nums[i])
            res[i] = index
        return res

    def countSmaller(self, nums):
        original = nums[:]
        length = len(nums)
        res = [0] * length

        def helper(s, e):
            if s+1 >= e:
                return

            m = (e - s) // 2 + s
            helper(s, m)
            helper(m, e)

            for i in range(s, m):
                index = bisect.bisect_left(nums[m:e], original[i]) #here we must use original[i] to do search, because nums already changed
                res[i] += index

            l, r = nums[s:m], nums[m:e]
            i, j, k = 0, 0, s
            while i < len(l) and j < len(r):
                if l[i] > r[j]:
                    nums[k] = r[j]
                    j += 1
                else:
                    nums[k] = l[i]
                    i += 1
                k += 1
            while i < len(l):
                nums[k] = l[i]
                i += 1
                k += 1
            while j < len(r):
                nums[k] = r[j]
                j += 1
                k += 1

        helper(0, length)
        return res
