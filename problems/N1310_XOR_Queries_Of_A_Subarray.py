class Solution(object):
    def xorQueries_myself(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        length = len(arr)
        prefix = [[0]*32 for _ in range(length+1)]
        for i, num in enumerate(arr):
            for j in range(32):
                if (num >> j) & 1:
                    prefix[i+1][j] += 1 + prefix[i][j]
                else:
                    prefix[i+1][j] += prefix[i][j]

        res = [0] * len(queries)
        for index, li in enumerate(queries):
            val = 0
            i, j = li
            for k in range(32):
                if (prefix[j+1][k] - prefix[i][k]) % 2:
                    val += 2 ** k
            res[index] = val
        return res

    """
    x^y^z^x == x^x^y^z == 0^y^z == y^z
    """
    def xorQueries(self, arr, queries):
        length = len(arr)
        prefix = [0] * (length+1)
        for i in range(length):
            prefix[i+1] = prefix[i] ^ arr[i]
        res = []
        for i, j in queries:
            res.append(prefix[j+1]^prefix[i])
        return res