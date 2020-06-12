import bisect
import collections


class Solution(object):
    # binary search
    # time complexity is o(n*n)
    # list.pop is o(n)
    def advantageCount_myself(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sorted_a = sorted(A)
        res = []
        for i in B:
            index = bisect.bisect(sorted_a, i)
            if index == len(sorted_a):
                res.append(sorted_a.pop(0))
            else:
                res.append(sorted_a[index])
                sorted_a.pop(index)
        return res

    # o(nlgn)
    def advantageCount(self, A, B):
        sorted_a = sorted(A)
        sorted_b = sorted(B)
        mapping = collections.defaultdict(list)
        for b in sorted_b[::-1]:
            if b < sorted_a[-1]:
                mapping[b].append(sorted_a.pop())
        return [(mapping[b] or A).pop() for b in B]
