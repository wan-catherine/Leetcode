class Solution(object):
    def findLength_dp(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if not A or not B:
            return 0

        a_len = len(A)
        b_len = len(B)
        dp_table = [[None]*a_len for _ in range(b_len)]

        res = 0
        for i in range(0,b_len):
            for j in range(0,a_len):
                if A[j] != B[i]:
                    dp_table[i][j] = 0
                else:
                    if i == 0 or j ==0:
                        dp_table[i][j] = 1
                    else:
                        dp_table[i][j] = dp_table[i-1][j-1] + 1
                res = max(res, dp_table[i][j])
        return res

    # binary search
    def findLength(self, A, B):
        def check(length):
            seen = set(tuple(A[i:i + length])
                       for i in range(len(A) - length + 1))
            print(seen)
            print (set(tuple(B[j:j + length]) for j in range(len(B) - length + 1)))
            return any(tuple(B[j:j + length]) in seen
                       for j in range(len(B) - length + 1))

        lo, hi = 0, min(len(A), len(B))
        while lo <= hi:
            mi = lo + (hi - lo) // 2
            if check(mi):
                lo = mi + 1
            else:
                hi = mi - 1
        return lo - 1