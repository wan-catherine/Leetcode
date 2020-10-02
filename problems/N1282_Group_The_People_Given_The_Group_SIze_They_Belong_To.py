import collections


class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        res = []
        mapping = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            mapping[size].append(i)

        keys = sorted(mapping.keys())
        for size in keys:
            l = 0
            while l < len(mapping[size]):
                res.append(mapping[size][l:l+size])
                l += size
        return res



