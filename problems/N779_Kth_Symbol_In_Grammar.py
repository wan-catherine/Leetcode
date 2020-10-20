class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N <= 2:
            return 0 if K % 2 else 1

        k = K-1
        n = N - 1
        while n > 1:
            num = 2 ** n
            if num // 2 > k:
                num //= 2
            else:
                if k < num // 2 + num // 4:
                    num //= 2
                    k = k - num + num//2
                else:
                    num //= 2
                    k = k - num - num//2
            n -= 1
        return k



