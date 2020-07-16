import collections


class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        length = len(arr)
        counts = collections.Counter(arr)
        res = 0
        count = 0
        for i, num in counts.most_common(length//2):
            count += num
            res += 1
            if count >= length // 2:
                return res

