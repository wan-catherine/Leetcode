import collections
from typing import List


class Solution:
    def beautifulSubsets_TLE(self, nums: List[int], k: int) -> int:
        length = len(nums)
        memo = {}
        def dfs(cur, status):
            if cur == length:
                return 1
            if (cur, status) in memo:
                return memo[(cur, status)]
            flag = True
            for i in range(cur):
                if ((status >> i) & 1) and abs(nums[cur] - nums[i]) == k:
                    flag = False
                    break
            take = dfs(cur + 1, status + (1 << cur))
            notake = dfs(cur + 1, status)
            if flag:
                res = take + notake
            else:
                res = notake
            memo[(cur, status)] = res
            return res
        return dfs(0, 0) - 1

    """
    1. split into k buckets which keys are (0, 1, ..., k-1), each of the buckets don't influence each other 
    2. in each buckets , it similar like house rob (DP)
    """
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        counter = collections.defaultdict(int)
        for n in nums:
            counter[n] += 1
        buckets = collections.defaultdict(list)
        for n in counter.keys():
            buckets[n % k].append(n)
        # print(buckets)
        res = 1
        for _, li in buckets.items():
            li.sort()
            length = len(li)
            take, notake = 0, 1
            for i in range(length):
                ct, cn = take, notake
                if i > 0 and li[i] - li[i-1] == k:
                    take = cn * ((1 << counter[li[i]]) - 1)
                    notake = ct + cn
                else:
                    take = (ct + cn) * ((1 << counter[li[i]]) - 1)
                    notake = ct + cn
            res *= (take + notake)
        return res - 1