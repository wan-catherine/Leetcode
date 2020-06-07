"""
Too compliated .
Use merge sort

"""
from bisect import bisect_left, bisect_right, insort_left


class Solution(object):
    def countRangeSum_slow(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sum = [0] + nums
        nums_len = len(nums)
        for i in range(nums_len):
            sum[i+1] = sum[i] + nums[i]
        count = self.merge_sort(sum, 0, nums_len, lower, upper)
        return count

    def merge_sort(self, sum, start, end, lower, upper):
        if end <= start:
            return 0
        mid = (end - start) // 2 + start
        count = self.merge_sort(sum, start, mid, lower, upper) + self.merge_sort(sum, mid + 1, end, lower, upper)
        lo, hi = mid + 1, mid + 1
        for i in range(start, mid + 1):
            while lo <= end and sum[lo] - sum[i] < lower:
                lo +=1
            while hi <= end and sum[hi] - sum[i] <= upper:
                hi += 1
            count += hi - lo
        self.merge(sum, start, mid + 1, end)
        return count

    def merge(self, sum, start, mid, end):
        cache = sum[:]
        l , r , index = start, mid, start
        while l < mid and r <= end:
            if cache[l] < cache[r]:
                sum[index] = cache[l]
                l += 1
            else:
                sum[index] = cache[r]
                r += 1
            index += 1
        while l < mid:
            sum[index] = cache[l]
            l += 1
            index += 1
        while r <= end:
            sum[index] = cache[r]
            r += 1
            index += 1

    # don't understand this method
    # it seems similar as #315 , but why ?????
    def countRangeSum(self, nums, lower, upper):
        if len(nums) == 0:
            return 0
        sums = [0, ]
        base = 0
        rgs = 0
        for i in range(len(nums)):
            base += nums[i]
            lpos = bisect_left(sums, lower - base)
            rpos = bisect_right(sums, upper - base)
            rgs += rpos - lpos
            insort_left(sums, -base)
        return rgs

