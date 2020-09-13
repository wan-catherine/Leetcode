import collections


class Solution(object):
    # faster than DP
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m and not n or not strs:
            return 0

        self.memo = {}
        mapping = collections.defaultdict(int)
        for s in strs:
            counter = collections.Counter(s)
            if counter['0'] > m or counter['1'] > n:
                continue
            mapping[(counter['0'], counter['1'])] += 1

        return self.dfs(m, n, mapping, 0)

    def dfs(self, m, n, mapping, val):
        # if (m, n) shows before and it's value > val, then we will use it !
        if (m, n) in self.memo and self.memo[(m, n)] > val:
            return self.memo[(m, n)]

        max_val = val
        for k, c in mapping.items():
            if k[0] <= m and k[1] <= n and c > 0:
                mapping[k] -= 1
                max_val = max(max_val, self.dfs(m-k[0], n-k[1], mapping, val+1))
                mapping[k] += 1
        self.memo[(m, n)] = max_val
        return max_val

    def findMaxForm_dp(self, strs, m, n):
        if not m and not n or not strs:
            return 0
        dp = [[0]*(n+1) for _ in range(m+1)]
        for s in strs:
            counter = collections.Counter(s)
            ones, zeroes = counter['1'], counter['0']

            for i in range(m, zeroes-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeroes][j-ones]+1)
        return dp[-1][-1]

    def findMaxForm_others(self, strs, m, n):
        cnt = collections.Counter((s.count('0'), s.count('1')) for s in strs)
        count = sorted([k + (v,) for k, v in cnt.items() if k[0] <= m and k[1] <= n], key=lambda a: a[0] + a[1])
        memo = collections.defaultdict()

        def dfs(i, m_cnt, n_cnt, cur):
            mask = (i << 16) + (m_cnt << 8) + n_cnt
            if mask in memo:
                return memo[mask]
            if i == len(count) or count[i][0] + count[i][1] > m + n:
                memo[mask] = cur
            else:
                memo[mask] = max(dfs(i + 1, m_cnt - k * count[i][0], n_cnt - k * count[i][1], cur + k)
                                 for k in range(count[i][2], -1, -1)
                                 if m_cnt >= k * count[i][0] and n_cnt >= k * count[i][1])
            return memo[mask]

        return dfs(0, m, n, 0)