import collections


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ab_dict = collections.defaultdict(int)
        cd_dict = collections.defaultdict(int)
        res = 0
        for i in A:
            for j in B:
                ab_dict[i+j] += 1

        for i in C:
            for j in D:
                cd_dict[-i-j] += 1

        for key in ab_dict:
            if key in cd_dict:
                res += ab_dict[key] * cd_dict[key]
        return res
