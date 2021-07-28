class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        i = 0
        while (1 << i) <= label:
            i += 1
        res = [1] * i
        res[-1] = label
        while i > 2:
            if not i % 2:
                val = (1 << i) - 1 - label + (1 << (i-1))
                label = val // 2
            else:
                val = label // 2
                label = (1 << (i-2)) + (1 << (i-1)) - 1 - val
            res[i-2] = label
            i -= 1
        return res
