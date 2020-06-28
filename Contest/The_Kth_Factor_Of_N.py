class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if k == 1:
            return 1

        count = 0
        for i in range(1, n+1):
            value = n%i
            if not value:
                count += 1
                if count == k:
                    return i
        return -1