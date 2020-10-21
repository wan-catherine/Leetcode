import collections


class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        arr = sorted(A)
        s = set(arr)

        dp = collections.defaultdict(int)
        for i, v in enumerate(arr):
            dp[v] = 1
            visited = set()
            for j in range(i):
                if v % arr[j] == 0 and arr[j] not in visited:
                    val = v // arr[j]
                    if val not in s or val in visited:
                        continue
                    visited.add(v)
                    visited.add(val)
                    dp[v] += dp[arr[j]] * dp[val] * (2 if arr[j] != val else 1)
        print(dp)
        return sum(dp.values()) % (10**9 + 7)

