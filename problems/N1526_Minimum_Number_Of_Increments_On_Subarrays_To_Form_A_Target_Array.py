class Solution(object):
    def minNumberOperations_others(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        res = 0
        for a, b in zip([0] + target, target):
            res += max(0, b - a)
        return res

    def minNumberOperations(self, target):
        res = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                res += target[i] - target[i - 1]
        return res