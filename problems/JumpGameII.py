from typing import List


class Solution:
    def jump_timeout(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        path = []
        while 0 not in path:
            if len(path) == 0:
                lastpos = len(nums) - 1
            else:
                lastpos = path[-1]
            for i in range(lastpos):
                if nums[i] >= lastpos - i:
                    break
            path.append(i)

        return len(path)

    def jump_DP(self, nums):
        if nums == None or len(nums) < 2:
            return 0

        res = [0] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] >= i - j and (res[i] == 0 or res[j] + 1 < res[i]):
                    res[i] = res[j] + 1
        return res[-1]

    def jump_dfs(self, nums):
        if nums == None or len(nums) < 2:
            return 0
        # still timeout , need to deal with [1,1,...,1] specially
        if set(nums) == {1}:
            return len(nums) - 1

        level = 0
        cur = [0]
        next = []
        end = len(nums) - 1
        while True:
            for i in cur[::-1]:
                for j in range(1, nums[i] + 1):
                    if i + j == end:
                        return level + 1
                    if i + j in cur:
                        continue
                    else:
                        next.append(i+j)
            level += 1
            cur = next

    def jump(self, nums):
        if nums is None:
            return 0
        n = len(nums)
        level = 0
        current_end = 0
        current_farthest = 0
        for i in range(n):
            if current_end == n - 1:
                break
            if i + nums[i] > current_farthest:
                current_farthest = i + nums[i]
            if i == current_end:
                level = level + 1
                current_end = current_farthest
        return level

    def jump_easy(self, nums):
        if len(nums) <= 1: return 0
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt
        return times

    """
    O(N) DP
    dp[i] : arrive position i, need the minimum jump . 
        dp[i] = min(dp[i-k],...,dp[i+3],dp[i+2],dp[i+1]) + 1 
        let's check : min(dp[i-k],...,dp[i+3],dp[i+2],dp[i+1]) == dp[i-k]
        
        because , when we arrive i, use dp[i] jump, if we want to arrive i + 1, we won't use less than dp[i] jumps . 
        dp[i+1] will be dp[i] or dp[i] + 1 
        ==> dp[i-k] <= ... <= dp[i+3] <= dp[i+2] <= dp[i+1] 
        
        then we need to calculate the most far position from i which can jump directly to i . 
        
    """
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        dis = [0] * length
        j = 0
        for i in range(1, length):
            while j + nums[j] < i:
                j += 1
            dis[i] = j
        dp = [0] * length
        for i in range(1, length):
            dp[i] = dp[dis[i]] + 1
        return dp[-1]




