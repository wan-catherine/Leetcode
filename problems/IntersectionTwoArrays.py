class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        if nums1 == None or nums2 == None:
            return []

        s1 = sorted(set(nums1))
        s2 = sorted(set(nums2))

        i = 0
        j = 0
        res = []
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                res.append(s1[i])
                i += 1
                j += 1
            elif s1[i] > s2[j]:
                j += 1
            elif s1[i] < s2[j]:
                i += 1

        return res

