import collections

"""
Greedy. 
decrease the larger one, and increase the smaller one
"""

class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2:
            return 0
        if s1 > s2 :
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1

        diff, res = s2 - s1, 0
        count1, count2 = collections.Counter(nums1), collections.Counter(nums2)

        for val in range(5, 0, -1):
            while count1[6-val]:
                diff -= val
                count1[6 - val] -= 1
                res += 1
                if diff <= 0:
                    return res

            while count2[val + 1]:
                diff -= val
                count2[val+1] -= 1
                res += 1
                if diff <= 0:
                    return res
        return -1

