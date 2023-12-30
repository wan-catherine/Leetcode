from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        length = len(nums1)
        def helper(first, second):
            count = 0
            for i in range(length-2, -1, -1):
                if first[i] <= first[-1] and second[i] <= second[-1]:
                    continue
                if first[i] <= second[-1] and second[i] <= first[-1]:
                    count += 1
                    continue
                count = -1
                break
            return count

        a = helper(nums1, nums2)
        b = helper(nums1[:-1] + [nums2[-1]], nums2[:-1] + [nums1[-1]])
        if a == -1 and b == -1:
            return -1
        if a == -1:
            return b + 1
        if b == -1:
            return a
        return min(a, b + 1)