import collections


class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        res = 0
        for n in nums1:
            res += self.helper(n*n, nums2)
        for n in nums2:
            res += self.helper(n*n, nums1)
        return res

    def helper(self, n, nums):
        d_nums = collections.defaultdict(int)
        count = 0
        for i in nums:
            if not n % i:
                count += d_nums[n//i]
                d_nums[i] += 1
        return count
