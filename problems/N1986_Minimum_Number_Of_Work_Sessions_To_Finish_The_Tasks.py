import sys
from typing import List


class Solution:
    # almost TLE :P
    def minSessions_(self, tasks: List[int], sessionTime: int) -> int:
        length = len(tasks)
        tasks.sort(reverse=True)
        km = sum(tasks) // sessionTime
        def check(idx, cur, l):
            if idx == length:
                for val in cur:
                    if val > sessionTime:
                        return False
                return True

            for i in range(l):
                if cur[i] + tasks[idx] <= sessionTime:
                    cur[i] += tasks[idx]
                    if check(idx +1, cur[:], l):
                        return True
                    cur[i] -= tasks[idx]
            return False

        for k in range(km, length):
            ks = [0] * k
            if check(0, ks, k):
                return k
        return length

    """
    Surprise, this loop subset method in leetcode TLE!!!
    Anyway , when we see : 1 <= n <= 14, we know it's NP problem.
    3**14 is an acceptable time complexity. 
    Then we consider loop subset which is o(3**n)
    """
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        length = len(tasks)
        dp = [sys.maxsize] * (1 << length)
        for status in range(0, 1 << length):
            cur = 0
            for i in range(length):
                if (status >> i) & 1:
                    cur += tasks[i]
            if cur <= sessionTime:
                dp[status] = 1
        for status in range(0, 1 << length):
            subset = status
            while subset > 0:
                dp[status] = min(dp[status], dp[subset] + dp[status - subset])
                subset = (subset - 1) & status
        return dp[-1]