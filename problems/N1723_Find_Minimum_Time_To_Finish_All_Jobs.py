import collections
import sys


class Solution(object):
    def minimumTimeRequired_status_compression_tle(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
        length = len(jobs)
        times = collections.defaultdict(int)
        for state in range(1 << length):
            t,i = 0, length - 1
            key = state
            while state:
                if state&1:
                    t += jobs[i]
                state >>= 1
                i -= 1
            times[key] = t

        dp = [[sys.maxsize]*(1 << length) for _ in range(k+1)]
        dp[0][0] = 0

        for i in range(1, k+1):
            for state in range(1 << length):
                j = state
                while j:
                    dp[i][state] = min(dp[i][state], max(dp[i-1][state-j], times[j]))
                    j = (j - 1) & state
        return dp[-1][-1]

    def minimumTimeRequired_state_binary_search_tle(self, jobs, k):
        total = sum(jobs)
        length = len(jobs)
        times = collections.defaultdict(int)

        for state in range(1 << length):
            t, i = 0, length - 1
            key = state
            while state:
                if state & 1:
                    t += jobs[i]
                state >>= 1
                i -= 1
            times[key] = t

        def dfs(val, cur, n):
            if cur == 0:
                return True
            if n == k:
                return False
            if visited[n][cur]:
                return False
            j = cur
            while j:
                if times[j] <= val and dfs(val, cur - j, n+1):
                    return True
                j = (j-1)&cur
            visited[n][cur] = 1
            return False

        l, r = 0, total
        while l < r:
            visited = [[0] * (1 << length) for _ in range(k + 1)]
            m = (r - l) // 2 + l
            if dfs(m, (1 << length)-1, 0):
                r = m
            else:
                l = m + 1
        return l

    def minimumTimeRequired(self, jobs, k):
        jobs.sort(reverse=True)
        length = len(jobs)

        # the flag is an very efficient prune .
        # for those k workers, we can treat them as no different container .
        # so for the first trying, we put any of them are the same. so we can actually save (k-1)/k time.
        def dfs(val, index):
            nonlocal length
            flag = 0
            if index == length:
                return True
            for i in range(k):
                if workers[i] == 0:
                    if flag == 1:
                        continue
                    flag = 1
                if workers[i] + jobs[index] <= val:
                    workers[i] += jobs[index]
                    if dfs(val, index+1):
                        return True
                    workers[i] -= jobs[index]
            return False

        l, r = 0, sum(jobs)
        while l < r:
            workers = [0] * k
            m = (r - l) // 2 + l
            if dfs(m, 0):
                r = m
            else:
                l = m + 1
        return l
