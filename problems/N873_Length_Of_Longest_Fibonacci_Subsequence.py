class Solution(object):
    def lenLongestFibSubseq_pair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        value_index_mapping = {}
        length = len(A)
        for i in range(length):
            value_index_mapping[A[i]] = i
        res = 0
        for i in range(length):
            for j in range(i+1,length):
                a, b, fib = A[i], A[j], A[i] + A[j]
                count = 2
                while fib in value_index_mapping:
                    a, b, fib = b, fib, b + fib
                    count += 1
                res = max(res, count)
        return res if res > 2 else 0

    def lenLongestFibSubseq_dp(self, A):
        length = len(A)
        dp = [[2] * length for _ in range(length)]
        value_index_mapping = {}
        res = 0
        for i in range(length):
            value_index_mapping[A[i]] = i
        for i in range(length):
            for j in range(i+1, length):
                fib = A[j] - A[i]
                if fib >= A[i]:  #here must to avoid fib == A[i], A is a strictly increasing array
                    break
                if fib not in value_index_mapping:
                    continue
                dp[i][j] = dp[value_index_mapping[fib]][i] + 1
                res = max(res, dp[i][j])
        return res