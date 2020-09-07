class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = int(s, 2)
        step = 0
        while num != 1:
            if num % 2:
                num += 1
            else:
                num //= 2
            step += 1
        return step