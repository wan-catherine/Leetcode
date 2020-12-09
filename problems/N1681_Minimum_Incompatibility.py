import collections
import sys
from functools import lru_cache
from itertools import combinations


class Solution:
    def minimumIncompatibility_wrong(self, nums, k: int) -> int:
        length = len(nums)
        count = [0]*(length+1)
        for n in nums:
            count[n] += 1
            if count[n] > k:
                return  -1
        if k == 1:
            return 0

        time = length // k
        res = [set() for _ in range(k)]
        ans = sys.maxsize
        visited = [0]* length
        def dfs(j):
            nonlocal ans
            if j == k:
                cur = 0
                for s in res:
                    cur += max(s) - min(s)
                ans = min(ans, cur)
                return
            for i in range(1, length+1):
                if not count[i] or i in res[j]:
                    continue
                count[i] -= 1
                res[j].add(i)
                if len(res[j]) == time:
                    dfs(j+1)
                else:
                    dfs(j)
                res[j].remove(i)
                count[i] += 1
        dfs(0)
        return ans

    def minimumIncompatibility_(self, nums, k: int) -> int:
        n = len(nums)
        size = n // k

        @lru_cache(None)
        def dp(mask):
            if mask == (1 << n) - 1:
                return 0

            ans = sys.maxsize
            remaining = [i for i in range(n) if mask & (1<<i) == 0]
            comb = list(combinations(remaining, size))

            for c in comb:
                cur = set([nums[i] for i in c])
                if len(cur) < size:
                    continue
                new_mask = mask
                for i in c:
                    new_mask |= (1 << i)
                ans = min(ans, dp(new_mask) + max(cur) - min(cur))
            return ans

        ans = dp(0)
        return ans if ans < sys.maxsize else -1

    def minimumIncompatibility_tle(self, nums, k: int) -> int:
        times = collections.Counter(nums)
        length = len(nums)
        for _, v in times.items():
            if v > k:
                return -1

        nums.sort()
        visited = [0] * length
        res = sys.maxsize
        t = length // k
        def dfs(index, count, low, high, total):
            nonlocal res
            if count == t:
                j = 0
                while j< length and visited[j]:
                    j += 1
                if j == length:
                    res = min(res, total + high - low)
                    return
                visited[j] = 1
                dfs(j, 1, nums[j], nums[j], total + high - low)
                visited[j] = 0
            else:
                last = -1
                for i in range(index+1, length):
                    if visited[i]:
                        continue
                    if i > index + 1 and last == nums[i]:
                        continue
                    if nums[i] == nums[index]:
                        continue
                    visited[i] = 1
                    dfs(i, count+1, low, nums[i], total)
                    last = nums[i]
                    visited[i] = 0
        visited[0] = 1
        dfs(0, 1, nums[0], nums[0], 0)
        return res

    def minimumIncompatibility_fast(self, nums, k: int) -> int:
        f = collections.Counter(nums)
        if any(f[num] > k for num in f):
            return -1
        bags = [[] for i in range(k)]
        res = float("inf")
        n = len(nums)
        M = n // k
        nums.sort()

        def DFS(i, cur_res):
            nonlocal res
            if i == n:
                res = min(res, cur_res)
                return
            if cur_res >= res - (n + 1 - i):
                return

            for j in range(k):
                if (j > 0 and bags[j] == bags[j - 1]) or (bags[j] and bags[j][-1] == nums[i]) or (len(bags[j]) == M):
                    continue
                else:
                    bags[j].append(nums[i])
                    if len(bags[j]) == 1:
                        DFS(i + 1, cur_res)
                    else:
                        # 1,2,5 ==> 2-1 + 5-2 = 5-2+(2-1) = 5-1
                        DFS(i + 1, cur_res + bags[j][-1] - bags[j][-2])
                    bags[j].pop()

        DFS(0, 0)
        return res

    def minimumIncompatibility(self, nums, k: int) -> int:
        f = collections.Counter(nums)
        if any(f[num] > k for num in f):
            return -1
        length = len(nums)
        dp = [[sys.maxsize] * length for _ in range(1<<length) ]
        for i in range(length):
            dp[1<<i][i] = 0
        c = length // k
        # nums.sort()
        for state in range(1<<length):
            for last_idx in range(length):
                if (state & (1 << last_idx)) == 0:
                    continue
                for new_idx in range(length):
                    if (state & (1 << new_idx)):
                        continue
                    # if nums[last_idx] == nums[new_idx]:
                    #     continue
                    new_state = (state | (1 << new_idx))
                    t = state
                    chose_num_count = 0
                    while t:
                        chose_num_count += (t % 2)
                        t //= 2
                    if chose_num_count % c == 0:
                        dp[new_state][new_idx] = min(dp[new_state][new_idx], dp[state][last_idx])
                    elif nums[new_idx] > nums[last_idx]:
                        dp[new_state][new_idx] = min(dp[new_state][new_idx], dp[state][last_idx] + nums[new_idx] - nums[last_idx])
        return min(dp[-1])









