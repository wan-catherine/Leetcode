class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)

        i = 0
        j = 0
        res = []

        while i < len1 and j < len2:
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        if i < len1:
            res.extend(nums1[i:])
        elif j < len2:
            res.extend(nums2[j:])

        index = (len1 + len2) // 2
        if (len1 + len2) % 2 != 0:
            median = res[index]
        else:
            median = (res[index - 1] + res[index]) / 2

        return median
