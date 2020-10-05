class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        memo = {}
        def get_power(n):
            if n in memo:
                return memo[n]
            res = 0
            while n != 1:
                if n % 2:
                    n = 3 * n + 1
                else:
                    n = n // 2
                res += 1
            memo[n] = res
            return memo[n]

        mapping = [(get_power(i), i) for i in range(lo, hi+1)]
        mapping.sort()
        return mapping[k-1][1]
