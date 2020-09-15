import bisect
import collections


class Solution(object):
    def findNumberOfLIS_TLE(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, ans = 0, 0
        stack = []
        mapping = collections.defaultdict(list)
        for i, c in enumerate(nums):
            index = bisect.bisect_left(stack, c)
            bisect.insort_left(stack, c)
            if index == 0:
                mapping[c].append([i, 1, 1])
                res = max(res, 1)
                continue

            count = 1
            for j in range(index):
                for li in mapping[stack[j]]:
                    count = max(count, li[1] + 1)
            nums = 0
            previous = None
            for j in range(index):
                if stack[j] == previous:
                    continue
                previous = stack[j]
                for li in mapping[stack[j]]:
                    if li[1] == count - 1:
                        nums += li[2]

            mapping[c].append([i, count, nums])
            if count > res:
                res = count
        for key, li in mapping.items():
            for _,c,n in li:
                if c == res:
                    ans += n
        return ans

    def findNumberOfLIS(self, nums):
        if not nums:
            return 0
        length = len(nums)
        dp = [1] * length
        times = [1] * length
        ans = 1
        max_len = 0
        for i, c in enumerate(nums):
            for j in range(i):
                if nums[j] >= c:
                    continue
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    times[i] = times[j]
                elif dp[i] == dp[j] + 1:
                    times[i] += times[j]
            if max_len == dp[i]:
                ans += times[i]
            if max_len < dp[i]:
                max_len = dp[i]
                ans = times[i]
        print(dp, times)
        return ans

